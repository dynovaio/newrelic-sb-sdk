__all__ = ["Page"]


from dataclasses import dataclass
from datetime import datetime
from typing import List

from ..core.base import BaseEntity
from .utils import OwnerInfo
from .widgets import Widget


@dataclass(kw_only=True)
class Page(BaseEntity):
    guid: str | None = None
    name: str
    description: str | None = None
    widgets: List[Widget]
    owner: OwnerInfo | None = None

    created_at: datetime | None = None
    updated_at: datetime | None = None

    property_processors = {
        "owner": OwnerInfo.from_json,
        # "created_at": lambda json_str: datetime.strptime(
        #     json.loads(json_str), "%Y-%m-%dT%H:%M:%SZ"
        # ).replace(tzinfo=timezone.utc)
        # if json.loads(json_str)
        # else None,
        # "updated_at": lambda json_str: datetime.strptime(
        #     json.loads(json_str), "%Y-%m-%dT%H:%M:%SZ"
        # ).replace(tzinfo=timezone.utc)
        # if json.loads(json_str)
        # else None,
    }
