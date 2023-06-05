__all__ = ["generate_nrql_query_string", "generate_clauses", "get_function_by_metric"]


def generate_nrql_query_string(function, event, clauses=None):
    if clauses is None:
        return f"FROM {event} SELECT {function}"

    return f"FROM {event} SELECT {function} {clauses}"


def generate_clauses(condition_scope, apps_names):
    if condition_scope == "application":
        names = ", WHERE appName LIKE ".join([f"'%{app}%'" for app in apps_names])
        return f"FACET CASES( WHERE appName LIKE {names} )"
    return ""


def get_function_by_metric(metric):
    if metric == "error_percentage":
        return "percentage(count(*), WHERE error IS TRUE)"

    if metric == "response_time_web":
        return "apdex(duration, t: 0.5)"

    return "count(*)"
