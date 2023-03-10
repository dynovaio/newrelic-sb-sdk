__all__ = ["Dashboard"]


import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import List

from ..core.base import BaseEntity
from ..utils.text import camelize_keys, snakeize_keys
from .enums import DashboardPermission
from .pages import Page
from .utils import OwnerInfo


@dataclass(kw_only=True)
class Dashboard(BaseEntity):
    guid: str | None = None
    account_id: int | None = None

    name: str
    description: str = ""
    pages: List[Page]
    permissions: DashboardPermission

    owner: OwnerInfo | None = None

    created_at: datetime | None = None
    updated_at: datetime | None = None

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
