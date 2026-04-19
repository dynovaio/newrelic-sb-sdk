__all__ = ["logger", "USER_KEY_PATTERN", "validate_user_key"]


import logging
import re

logger = logging.getLogger("newrelic_sb_sdk")


USER_KEY_PATTERN: re.Pattern = re.compile("NRAK-[A-Z0-9]{27}")


def validate_user_key(user_key: str) -> bool:
    """Validate a New Relic user key against target signatures.

    Args:
        user_key: The string API key.

    Returns:
        True if the format matches standard configurations, False otherwise.
    """

    match: re.Match[str] | None = re.match(USER_KEY_PATTERN, user_key)

    return bool(match)
