import sys

from loguru import logger

from .app import main

logger_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": "<level>{module}:{line} ----- {level}: {message}</level>",  # noqa
        }
    ]
}


async def create_app():
    logger.configure(**logger_config)
    await main()
