import asyncio
import logging
from octopus.utils import clean_nones
from urllib.parse import urlencode
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-log", 
    "--log", 
    default="warning",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
)

options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)

async def main():
    # Get today's date
    today = datetime.today().replace(hour=21, minute=0)
    print("Today is: ", today)
    
    # Yesterday date
    tomorrow = today + timedelta(days = 1)
    print("tomorrow is: ", tomorrow)

    page = None

    params = urlencode(
        clean_nones(
            {"period_from": today.strftime('%d-%m-%YT%H:%MZ') or today, "period_to": tomorrow.strftime('%d-%m-%YT%H:%MZ') or tomorrow, "page": page}
        ), safe=':+'
    )
    logging.debug(f"params: {params}")

asyncio.run(main())
