import logging

from .version import VERSION

__version__ = "0.37.0"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
