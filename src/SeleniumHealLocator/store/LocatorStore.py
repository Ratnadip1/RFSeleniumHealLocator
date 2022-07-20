import threading


class LocatorStore(object):

    __lock = threading.Lock()
    __locatorInstance = None

    def __init__(self):
        self.locatorIndexDict = {}
        self.locatorDict = {}
        pass

    @classmethod
    def get_Instance(cls):
        if not cls.__locatorInstance:
            with cls.__lock:
                if not cls.__locatorInstance:
                    cls.__locatorInstance = cls()
        return cls.__locatorInstance

    def get_Locator_Id(self, page_id, locator):
        
        pass
