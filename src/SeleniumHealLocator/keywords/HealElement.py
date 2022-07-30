from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from ..store.PageStore import PageStore
from ..store.LocatorStore import LocatorStore
from ..store.LocatorInfo import LocatorInfo
from ..utilities.HealLog import HealLog
from ..exceptions.HealLocatorException import HealLocatorException
from ..evaluation.DOMEvaluation import DOMEvaluation

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

    # Constructor for HealElement initializing the locator evaluation process.
    def __init__(self):
        self.browser = None
        self.pageStore = PageStore.get_Instance()  # Singleton reference of PageStore object
        self.locatorStore = LocatorStore.get_Instance()  # Singleton reference of LocatorStore object.
        self.domEval = None
        self.logger = HealLog()
        pass

    @keyword
    def get_Heal_Locator(self, locator):
        try:
            # Initiates the browser instance by referencing the browser in the RobotFramework
            # SeleniumLibrary.
            if not self.browser:
                self.browser = HealElement.getFrameworkDriver()
            page_id = self.pageStore.get_Page_Info(self.browser.current_url)
            current_locator_info = LocatorInfo.process_locator(locator)
            self.logger.info('Strategy: ' + str(current_locator_info.get_strategy()))
            self.logger.info('Locator: ' + str(current_locator_info.get_locator()))
            self.domEval = DOMEvaluation(self.browser, current_locator_info)

            if self.domEval.validate_Element_Available_In_DOM():
                self.logger.info("Current Locator element for Locator Info {} is available in DOM."
                                 .format(str(current_locator_info)))
                page_id = self.pageStore.get_Page_Info(self.browser.current_url)
                is_locator_available = self.locatorStore.validate_Locator_Available(page_id, current_locator_info)
                if is_locator_available:
                    self.logger.info("Locator info for locator '{}' is already available".format(locator))
                    pass
                else:
                    self.locatorStore.add_Locator_ToDict(page_id, locator)
                    alternate_locator_list = self.domEval.evaluate_List_Of_Locator(current_locator_info)

                    pass
            else:
                self.logger.info("Current Locator element for Locator Info {} is not available in DOM."
                                 .format(str(current_locator_info)))
                pass
            #
        except HealLocatorException as exception:
            self.logger.error(exception)
        return locator

    # Method:       getFrameworkDriver
    # Type:         static
    # Description:  Retrieves the current Robot Framework browser on runtime
    #               to operate and evaluate alternate locators for the given locator.
    @staticmethod
    def getFrameworkDriver():
        try:
            selenium_library = BuiltIn().get_library_instance('SeleniumLibrary')
            browser = selenium_library.driver
        except Exception as exception:
            raise HealLocatorException('Error on getting Selenium Library instance/ browser reference from Robot Framework instance.')
        return browser
