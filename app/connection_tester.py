from . import config # For logger and potentially initial app imports via app.__init__
from .core import TESTER_REGISTRY

# Import app's __init__ to ensure all test modules are loaded and registered.
# This is crucial if not relying on other imports to trigger it.
from . import __init__ as app_initializer # Explicitly import to run registration

logger = config.get_logger(__name__)

def main():
    logger.info("--- Starting service connection tests (Refactored using Registration) ---")
    
    # Ensure app_initializer is used if linters complain about unused import
    _ = app_initializer 

    test_results = {}
    all_ok = True

    if not TESTER_REGISTRY:
        logger.warning("No testers registered! Check app/__init__.py and test module registrations.")
        return

    for service_name_key, TesterClass in TESTER_REGISTRY.items():
        tester_instance = TesterClass() # Instantiate the tester
        service_display_name = tester_instance.get_service_name() # Get actual display name
        
        logger.info(f"Testing {service_display_name} (Registered as: {service_name_key})...")
        try:
            if tester_instance.run_test():
                test_results[service_display_name] = "OK"
            else:
                test_results[service_display_name] = "FAILED"
                all_ok = False
        except Exception as e:
            logger.exception(f"An unexpected error occurred while running {service_display_name} test: {type(e).__name__} - {e}")
            test_results[service_display_name] = "ERROR (Framework)"
            all_ok = False

    logger.info("--- Service connection test summary ---")
    for service, status in test_results.items():
        logger.info(f"- {service}: {status}")
    
    if all_ok:
        logger.info("All services connected successfully!")
    else:
        logger.warning("Some services failed to connect. Please check logs above.")

if __name__ == "__main__":
    main() 