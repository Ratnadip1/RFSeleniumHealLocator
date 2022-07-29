from pathlib import Path

from ..evaluation.Strategy import Strategy


class LocatorInfo:

    def __init__(self, page_id=None, strategy=None, locator=None):
        self.page_id = page_id
        self.strategy = strategy
        self.locator = locator

    @classmethod
    def process_locator(cls, locator):
        locator_check = [':', '=']

        for format_check in locator_check:
            if locator.find(format_check) != -1:
                strategy = locator[0: locator.find(format_check)].strip()
                discreet_strategy = Strategy.get_Strategy_Type(strategy)
                if not discreet_strategy:
                    continue
                else:
                    locator = locator[locator.find(format_check) + 1:]
                    locator_info = cls(strategy=discreet_strategy, locator=locator)
                    break
                pass
            pass

        if not discreet_strategy:
            locator_info = cls(strategy=Strategy.xpath, locator=locator)
            pass
        return locator_info

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

