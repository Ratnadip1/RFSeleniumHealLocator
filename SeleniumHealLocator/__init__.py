from robotlibcore import DynamicCore
from SeleniumHealLocator.keywords import ManageInformation
from SeleniumHealLocator.utilities import ElementInformation


class SeleniumHealLocator(DynamicCore):

    def __init__(self):
        # self.element_info = None
        libraries = [
            ManageInformation(),
            ElementInformation()
        ]
        DynamicCore.__init__(self, libraries)
        for keyword in self.get_keyword_names():
            print("Keyword: " + keyword)

        pass




