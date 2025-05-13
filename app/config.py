import os
import logging

# --- Logging Configuration ---
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def get_logger(name):
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT) # Basic config for simplicity
    logger = logging.getLogger(name)
    return logger

# Ensure basicConfig is called only once if modules try to get logger multiple times,
# or configure it centrally in connection_tester.py. For now, this is simple.
# A more robust approach might involve a dedicated logging setup function called once.

# --- Service Connection Configurations ---

# MySQL Configuration
TEST_MYSQL_HOST = os.getenv('TEST_MYSQL_HOST', 'localhost')
TEST_MYSQL_USER = os.getenv('TEST_MYSQL_USER', 'testuser')
TEST_MYSQL_PASSWORD = os.getenv('TEST_MYSQL_PASSWORD', 'testpassword')
TEST_MYSQL_DB = os.getenv('TEST_MYSQL_DB', 'testdb')
TEST_MYSQL_CONNECT_TIMEOUT = int(os.getenv('TEST_MYSQL_CONNECT_TIMEOUT', '5'))

# Redis Configuration
TEST_REDIS_HOST = os.getenv('TEST_REDIS_HOST', 'localhost')
TEST_REDIS_PORT = int(os.getenv('TEST_REDIS_PORT', '6379'))

# Elasticsearch Configuration
TEST_ES_HOST = os.getenv('TEST_ES_HOST', 'localhost')
TEST_ES_PORT = int(os.getenv('TEST_ES_PORT', '9200'))
TEST_ES_URL = os.getenv('TEST_ES_URL', f"http://{TEST_ES_HOST}:{TEST_ES_PORT}")
# Elasticsearch in docker-compose has xpack.security.enabled=false, so no auth needed by default.

# Neo4j Configuration
TEST_NEO4J_URI = os.getenv('TEST_NEO4J_URI', 'bolt://localhost:7687')
TEST_NEO4J_USER = os.getenv('TEST_NEO4J_USER', 'neo4j')
TEST_NEO4J_PASSWORD = os.getenv('TEST_NEO4J_PASSWORD', 'testpassword') 