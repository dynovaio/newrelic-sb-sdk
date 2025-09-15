import logging

from .version import VERSION

__version__ = "0.39.0"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
