import pymysql
from . import config
from .core import ServiceTester, register_tester

logger = config.get_logger(__name__)

class MySQLTester(ServiceTester):
    def get_service_name(self) -> str:
        return "MySQL"

    def run_test(self) -> bool:
        conn = None
        try:
            logger.info(f"Attempting to connect to MySQL at {config.TEST_MYSQL_HOST} as {config.TEST_MYSQL_USER}...")
            conn = pymysql.connect(
                host=config.TEST_MYSQL_HOST,
                user=config.TEST_MYSQL_USER,
                password=config.TEST_MYSQL_PASSWORD,
                database=config.TEST_MYSQL_DB,
                connect_timeout=config.TEST_MYSQL_CONNECT_TIMEOUT
            )
            logger.info("MySQL OK")
            return True
        except pymysql.Error as e:
            logger.error(f"MySQL connection failed: {e}")
            return False
        except Exception as e:
            logger.exception(f"An unexpected error occurred with MySQL: {e}")
            return False
        finally:
            if conn:
                conn.close()

# Register this tester class
register_tester("MySQL", MySQLTester) 