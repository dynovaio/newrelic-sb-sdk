__all__ = ["Term", "Condition", "AlertCondition"]


from dataclasses import dataclass
from typing import Any, Dict, List, Union

from newrelic_sb_sdk.alerts.utils import (
    generate_clauses,
    generate_nrql_query_string,
    get_function_by_metric,
)

from ..core.base import BaseEntity


@dataclass(kw_only=True)
class Term(BaseEntity):
    operator: str
    priority: str
    threshold: int
    duration: int
    time_function: str


@dataclass(kw_only=True)
class Condition(BaseEntity):
    terms: Union[List[Term], Term]
    enabled: bool
    name: str


@dataclass(kw_only=True)
class AlertCondition(BaseEntity):
    account_id: Union[int, str]
    policy_id: Union[int, str]
    condition: Dict[str, Any]
    query: Union[str, None]
    query_kwargs: Union[Dict[str, Any], None]

    def generate_nrql_query(self):
        event = "Transaction"
        function = get_function_by_metric(self.condition["metric"])
        clauses = generate_clauses(
            self.condition["condition_scope"], self.condition["apps_names"]
        )

        return generate_nrql_query_string(function, event, clauses)

    def generate_query(self):
        query = ""
        if len(self.condition["terms"]) == 2:
            query = """
                mutation {
                  alertsNrqlConditionStaticCreate(
                    accountId: %(account_id)d,
                    policyId: %(policy_id)s,
                    condition: {
                        enabled: %(enabled)s,
                        nrql: {
                            query: "%(nrql_query)s",
                        },
                        name: "%(name_incident)s",
                        terms: [
                        {
                          operator: %(term0_operator)s,
                          priority: %(term0_priority)s,
                          threshold: %(term0_threshold)d,
                          thresholdDuration: %(term0_thresholdDuration)d,
                          thresholdOccurrences: %(term0_thresholdOccurrences)s
                        },
                        {
                          operator: %(term1_operator)s,
                          priority: %(term1_priority)s,
                          threshold: %(term1_threshold)d,
                          thresholdDuration: %(term1_thresholdDuration)d,
                          thresholdOccurrences: %(term1_thresholdOccurrences)s
                        }]
                    }
                    ){
                        enabled
                        name
                        id
                        policyId
                    }
                }
            """
        elif len(self.condition["terms"]) == 1:
            query = """
                mutation {
                  alertsNrqlConditionStaticCreate(
                    accountId: %(account_id)d,
                    policyId: %(policy_id)s,
                    conditions: {
                        enabled: %(enabled)s,
                        nrql: {
                            query: "%(nrql_query)s"
                        },
                        name: "%(name_incident)s",
                        terms: [
                        {
                          operator: %(term0_operator)s,
                          priority: %(term0_priority)s,
                          threshold: %(term0_threshold)d,
                          thresholdDuration: %(term0_thresholdDuration)d,
                          thresholdOccurrences: %(term0_thresholdOccurrences)s
                        }]
                    }
                    ){
                        id
                        enabled
                        name
                        policyId
                    }
                }
            """
        query_kwargs = {
            "account_id": self.account_id,
            "policy_id": self.policy_id,
            "enabled": "true" if self.condition["enabled"] else "false",
            "name_incident": self.condition["name"],
            "nrql_query": self.generate_nrql_query(),
        }

        for i, term in enumerate(self.condition["terms"]):
            query_kwargs.update(
                {
                    f"term{i}_operator": term["operator"].upper(),
                    f"term{i}_priority": term["priority"].upper(),
                    f"term{i}_threshold": int(term["threshold"]),
                    f"term{i}_thresholdDuration": int(term["duration"]) * 60,
                    f"term{i}_thresholdOccurrences": term["time_function"].upper(),
                }
            )

        self.query = query
        self.query_kwargs = query_kwargs

        return query % query_kwargs

    def create_alert(self, client):
        response = client.execute(query=self.query, query_kwargs=self.query_kwargs)
        response = response.json()
        return response["data"]["alertsNrqlConditionStaticCreate"]
