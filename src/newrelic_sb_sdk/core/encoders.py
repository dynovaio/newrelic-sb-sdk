__all__ = ["EntityEncoder"]


import json
from datetime import datetime
from enum import Enum


class EntityEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Enum):
            return o.value

        if isinstance(o, datetime):
            # Accoirding to newrelic dates are handled in
            # ISO8601 whithout microseconds and with Z as
            # time zone but python datetime.isoformat
            # doesn't workt in such way.
            # return obj.isoformat()
            # The user must be responsible for provide
            # obj in UTC timezone
            return o.strftime("%Y-%m-%dT%H:%M:%SZ")

        if hasattr(o, "__dict__"):
            return o.__dict__

        return super().default(o)
