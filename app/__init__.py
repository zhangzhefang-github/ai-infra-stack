# This file makes 'app' a Python package 

# Import test modules to trigger their registration decorators or calls
from . import test_mysql
from . import test_redis
from . import test_es
from . import test_neo4j

# Optionally, could expose parts of core or config here if desired
# from .core import TESTER_REGISTRY 