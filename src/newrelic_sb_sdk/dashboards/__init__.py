__all__ = ["Dashboard"]


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Union

from ..core.base import BaseEntity
from .enums import DashboardPermission
from .pages import Page
from .utils import OwnerInfo


@dataclass(kw_only=True)
class Dashboard(BaseEntity):
    guid: Union[str, None] = None
    account_id: Union[int, None] = None

    name: str
    description: str = ""
    pages: List[Page]
    permissions: DashboardPermission

    owner: Union[OwnerInfo, None] = None

    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

    property_processors = {
        "permissions": DashboardPermission.from_json,
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
