from robotlibcore import DynamicCore
from .keywords.ManageInformation import ManageInformation
from .keywords.HealElement import HealElement
from .utilities.ElementInformation import ElementInformation


class SeleniumHealLocator(DynamicCore):

    def __init__(self):
        # self.element_info = None
        libraries = [
            ManageInformation(),
            ElementInformation(),
            HealElement()
        ]
        DynamicCore.__init__(self, libraries)
        for keyword in self.get_keyword_names():
            print("Keyword: " + keyword)

        pass

