__all__ = ["BaseEnum", "BaseEntity"]


import json
from enum import Enum

from .mixins import SerializableMixin


class BaseEnum(SerializableMixin, Enum):
    def to_json(self, **kwargs) -> str:
        return json.dumps(self.value, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class BaseEntity(SerializableMixin):
    pass
