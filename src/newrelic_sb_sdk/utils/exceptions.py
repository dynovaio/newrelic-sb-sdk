__all__ = ["NewRelicError", "InvalidUserKey"]


from .validators import USER_KEY_PATTERN


class NewRelicError(Exception):
    """Base exception for New Relic API errors."""

    pass


class InvalidUserKey(ValueError):
    """Exception raised for invalid New Relic user keys."""

    def __init__(self, value):
        """Initialize the mapped exception.

        Args:
            value: The invalid property value configuring the internal boundaries.
        """

        self.value = value
        super().__init__(
            f"The provided key '{self.value}' does not match the format '{USER_KEY_PATTERN}'."
        )
