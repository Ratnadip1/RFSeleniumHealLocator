
class LocatorInfo:

    def __init__(self, page_id, strategy=None, locator=None):
        self.page_id = page_id
        self.strategy = strategy
        self.locator = locator

    def set_page_id(self, page_id):
        self.page_id = page_id

    def set_strategy(self, strategy):
        self.strategy = strategy

    def set_locator(self, locator):
        self.locator = locator

    def get_page_id(self):
        return self.page_id

    def get_strategy(self):
        return self.strategy

    def get_locator(self):
        return self.locator
    pass
