__all__ = ["Threshold", "NRQLQuery", "OwnerInfo"]


from dataclasses import dataclass
from typing import Union

from ..core.base import BaseEntity
from .enums import AlertSeverity


@dataclass(kw_only=True)
class Threshold(BaseEntity):
    alert_severity: AlertSeverity = AlertSeverity.CRITICAL
    value: Union[int, float] = 0

    property_processors = {
        "alert_severity": AlertSeverity.from_json,
    }


@dataclass(kw_only=True)
class NRQLQuery(BaseEntity):
    account_id: int
    query: str


@dataclass(kw_only=True)
class OwnerInfo(BaseEntity):
    user_id: int
    email: str
