from neo4j import GraphDatabase, exceptions
from . import config
from .core import ServiceTester, register_tester

logger = config.get_logger(__name__)

class Neo4jTester(ServiceTester):
    def get_service_name(self) -> str:
        return "Neo4j"

    def run_test(self) -> bool:
        driver = None
        try:
            logger.info(f"Attempting to connect to Neo4j at {config.TEST_NEO4J_URI} as user {config.TEST_NEO4J_USER}...")
            driver = GraphDatabase.driver(config.TEST_NEO4J_URI, auth=(config.TEST_NEO4J_USER, config.TEST_NEO4J_PASSWORD))
            with driver.session() as session:
                result = session.run("RETURN 1 AS result")
                if result.single():
                    logger.info("Neo4j OK")
                    return True
                else:
                    logger.warning("Neo4j query did not return expected result")
                    return False
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Neo4j connection failed (ServiceUnavailable): {e}")
            return False
        except exceptions.AuthError as e:
            logger.error(f"Neo4j authentication failed (AuthError): {e}")
            return False
        except Exception as e:
            logger.exception(f"An unexpected error occurred with Neo4j: {type(e).__name__} - {e}")
            return False
        finally:
            if driver:
                driver.close()

# Register this tester class
register_tester("Neo4j", Neo4jTester) 