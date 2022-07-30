from ..evaluation.Strategy import Strategy
from selenium.webdriver.common.by import By


class DOMEvaluation:

    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator
        pass

    def validate_Element_Available_In_DOM(self):
        locator_element = None
        strategy = self.locator.get_Strategy()
        if strategy == Strategy.id:
            locator_element = self.browser.find_elements(By.ID, self.locator)
        elif strategy == Strategy.name:
            locator_element = self.browser.find_elements(By.NAME, self.locator)
        elif strategy == Strategy.xpath:
            locator_element = self.browser.find_elements(By.XPATH, self.locator)
        elif strategy == Strategy.cssSelector:
            locator_element = self.browser.find_elements(By.CSS_SELECTOR, self.locator)
        elif strategy == Strategy.linkText:
            locator_element = self.browser.find_elements(By.LINK_TEXT, self.locator)
        elif strategy == Strategy.partialLinkText:
            locator_element = self.browser.find_elements(By.PARTIAL_LINK_TEXT, self.locator)
        elif strategy == Strategy.identifier:
            locator_element = self.browser.find_elements(By.ID, self.locator)
            if len(locator_element) == 0:
                locator_element = self.browser.find_elements(By.NAME, self.locator)
                pass
            pass
        if len(locator_element) > 0:
            return True
        else:
            return False

        pass
