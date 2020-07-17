import logging

try:
    from rich.logging import RichHandler

    # Setup the rich module.
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )
except ModuleNotFoundError:
    # If we are installing from setup.py for the first time then this 'rich'
    # module is unlikely to be installed, so for now don't worry about the log.
    pass

__version__ = "0.0.1"

from . import clustering
from . import clean
