import redis
from . import config # 导入新的配置模块
from .core import ServiceTester, register_tester

logger = config.get_logger(__name__) # 获取 logger 实例

class RedisTester(ServiceTester):
    def get_service_name(self) -> str:
        return "Redis"

    def run_test(self) -> bool:
        try:
            logger.info(f"Attempting to connect to Redis at {config.TEST_REDIS_HOST}:{config.TEST_REDIS_PORT}...")
            r = redis.Redis(
                host=config.TEST_REDIS_HOST,
                port=config.TEST_REDIS_PORT,
                socket_connect_timeout=5,
                decode_responses=True
            )
            r.ping() # 使用 ping() 检查连接
            r.set('app_ping', 'pong')
            if r.get('app_ping') == 'pong':
                logger.info("Redis OK (ping, set/get successful)")
                return True # 返回 True 表示成功
            else:
                logger.warning("Redis set/get check failed after successful ping")
                return False # 返回 False 表示失败
        except redis.exceptions.ConnectionError as e:
            logger.error(f"Redis connection failed: {e}")
            return False # 返回 False 表示失败
        except Exception as e:
            logger.exception(f"An unexpected error occurred with Redis: {e}")
            return False # 返回 False 表示失败

# Register this tester class
register_tester("Redis", RedisTester) 