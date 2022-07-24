from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from ..store.PageStore import PageStore

"""
HealElement performs the logic of finding 
"""


class HealElement(object):

    def __init__(self):
        self.browser = None
        self.pageStore = PageStore.get_Instance()
        pass

    @keyword
    def get_Heal_Locator(self, locator):
        # print("Title: " + self.browser.title)
        # print("Url: " + self.browser.current_url)

        # print("Locator: " + locator)
        page_id = self.pageStore.get_Page_Info(self.browser.current_url)
        page_id = PageStore.get_Page_Info(self.browser.current_url)
        return locator

    @staticmethod
    def getFrameworkDriver():
        try:
            selenium_library = BuiltIn().get_library_instance('SeleniumLibrary')
            browser = selenium_library.driver
        except Exception as exception:
            raise HealLocatorException('Error on getting Selenium Library instance.')
        return browser
