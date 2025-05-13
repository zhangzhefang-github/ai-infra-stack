from elasticsearch import Elasticsearch, ConnectionError
from . import config
from .core import ServiceTester, register_tester

logger = config.get_logger(__name__)

class ElasticsearchTester(ServiceTester):
    def get_service_name(self) -> str:
        return "Elasticsearch"

    def run_test(self) -> bool:
        try:
            logger.info(f"Attempting to connect to Elasticsearch at {config.TEST_ES_URL}...")
            es = Elasticsearch(config.TEST_ES_URL, request_timeout=5)
            if es.ping():
                logger.info("Elasticsearch OK")
                return True
            else:
                logger.warning("Elasticsearch ping failed")
                try:
                    health = es.cluster.health()
                    logger.info(f"Elasticsearch cluster health (though ping failed): {health}")
                except Exception as e_health:
                    logger.error(f"Failed to get Elasticsearch cluster health: {type(e_health).__name__} - {e_health}")
                return False
        except ConnectionError as e:
            logger.error(f"Elasticsearch connection failed (ConnectionError): {e}")
            if hasattr(e, 'info') and e.info:
                logger.error(f"Details: {e.info}")
            return False
        except Exception as e:
            logger.exception(f"An unexpected error occurred with Elasticsearch: {type(e).__name__} - {e}")
            return False

# Register this tester class
register_tester("Elasticsearch", ElasticsearchTester) 