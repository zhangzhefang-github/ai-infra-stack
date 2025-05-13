# app/core.py
import abc

TESTER_REGISTRY = {}

def register_tester(name, tester_class):
    if name in TESTER_REGISTRY:
        # Potentially log a warning if a tester name is overwritten
        pass 
    TESTER_REGISTRY[name] = tester_class # Store the class itself

class ServiceTester(abc.ABC):
    def __init__(self):
        # Logger can be initialized here if needed, or in subclasses
        # self.logger = config.get_logger(self.get_service_name()) 
        # This requires get_service_name() to be available at __init__ which might be tricky
        # Better to get logger in each subclass or pass config
        pass

    @abc.abstractmethod
    def get_service_name(self) -> str:
        """Return the human-readable name of the service."""
        pass

    @abc.abstractmethod
    def run_test(self) -> bool:
        """Execute the connection test for the service.
        Should handle its own logging for test steps.
        Returns True if successful, False otherwise.
        """
        pass 