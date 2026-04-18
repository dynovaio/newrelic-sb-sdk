__all__ = ["NewRelicError", "InvalidUserKey"]


from .validators import USER_KEY_PATTERN


class NewRelicError(Exception):
    pass


class InvalidUserKey(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f"The provided key '{self.value}' does not match the format '{USER_KEY_PATTERN}'."
        )
