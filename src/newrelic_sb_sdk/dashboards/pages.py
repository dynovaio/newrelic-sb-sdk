__all__ = ["Page"]


from dataclasses import dataclass
from datetime import datetime
from typing import List, Union

from ..core.base import BaseEntity
from .utils import OwnerInfo
from .widgets import Widget


@dataclass(kw_only=True)
class Page(BaseEntity):
    guid: Union[str, None] = None
    name: str
    description: Union[str, None] = None
    widgets: List[Widget]
    owner: Union[OwnerInfo, None] = None

    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

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
