"""Wait for postgres."""
import logging
import time

import psycopg2

from wait_for_utils.base import BaseReady
from wait_for_utils.config import DBConfig
from wait_for_utils.utils import get_interval_unit

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class PGReady(BaseReady):

    def is_ready(self, config: DBConfig) -> bool:
        while time.time() - self.start_time < config.check_timeout:
            try:
                conn = psycopg2.connect(
                    user=config.user,
                    password=config.password,
                    host=config.host,
                    port=config.port,
                    database=config.database
                )
                logger.info("PostgreSQL is ready!")
                conn.close()
                return True
            except psycopg2.OperationalError:
                logger.info(
                    "PostgreSQL is not ready yet. :( "
                    "Waiting %d %s for the next check...",
                    config.check_interval,
                    get_interval_unit(config.check_interval)
                )
                time.sleep(config.check_interval)
        return False
