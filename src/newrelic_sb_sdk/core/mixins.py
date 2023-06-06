__all__ = ["JSONMixin", "GQLMixin", "SerializableMixin"]


import json
from typing import Any, Dict, Union

from ..utils.text import camelize_keys, snakeize_keys
from .encoders import EntityEncoder


class JSONMixin:
    property_processors: Union[Dict[str, Any], None] = None

    @classmethod
    def _process_property(cls, property_name: str, json_str: str):
        if cls.property_processors is None:
            return json_str

        processor = cls.property_processors.get(property_name, None)

        if processor is None:
            return json_str

        return processor(json_str)

    @classmethod
    def _process_properties(cls, json_obj: dict):
        for property_name, processor in (cls.property_processors or {}).items():
            if property_name in json_obj:
                property_obj = json_obj[property_name]

                if isinstance(property_obj, list):
                    json_obj[property_name] = [
                        processor(json.dumps(item)) for item in property_obj
                    ]
                elif property_obj is not None:
                    json_obj[property_name] = processor(json.dumps(property_obj))

        return json_obj

    @classmethod
    def _load_json(cls, json_str: str) -> dict:
        json_obj = json.loads(json_str)

        if isinstance(json_obj, dict):
            json_obj = snakeize_keys(json_obj)
            json_obj = cls._process_properties(json_obj)

        return json_obj

    @staticmethod
    def _dumps_json(obj: dict, **kwargs) -> str:
        json_str = json.dumps(obj, cls=EntityEncoder)

        json_obj = json.loads(json_str)
        json_obj = camelize_keys(json_obj)

        json_str = json.dumps(json_obj, **kwargs)

        return json_str

    @classmethod
    def from_json(cls, json_str: str):
        json_obj = cls._load_json(json_str)

        if isinstance(json_obj, dict):
            return cls(**json_obj)

        return cls(json_obj)

    def to_json(self, **kwargs) -> str:
        return self._dumps_json(self.__dict__, **kwargs)


class GQLMixin:
    def get_gql_input(self):
        pass

    @property
    def gql(self) -> str:
        return ""


class SerializableMixin(GQLMixin, JSONMixin):
    pass
