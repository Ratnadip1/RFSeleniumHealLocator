from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from ..store.PageStore import PageStore

"""
HealElement performs the logic of evaluation and returning the locator that could be used to identify the WebElement.
If the locator is already available in LocatorStore, it checks if the current locator retrieves the WebElement correctly.
If the current locator is already available in Locator Store, it will not perform any action and return the original locator 
passed to *** Get Heal Element *** keyword. If the locator information is not available in the LocatorStore, the utility 
create a locator and add to LocatorStore. It will also evaluate the corresponding alternate locator and map it to the locator.
If the locator, passed to *** Get Heal Element *** keyword, does not retrieve (a) WebElement(s) in DOM, it checks the
LocatorStore for alternate locators that could retrieve the element. If the locator information is not available in the 
Element Information file, the locator returns the unchanged locator and the test script fails. If the locator information is 
available in the Element Information file, it evaluates the alternate locator, one by one and returns the first locator that 
can retrieve the element in DOM. The script will proceed the new locator and continue the execution. If there are no locators
that can retrieve an element in DOM, it returns the original locator sent as the parameter to *** Get Heal Element *** keyword 
and the script will fail.  
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
