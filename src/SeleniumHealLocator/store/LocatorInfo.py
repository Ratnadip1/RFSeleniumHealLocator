from ..evaluation.Strategy import Strategy

# LocatorInfo is used to create an object to store locator and alternate locator objects.
# It processes the current locator and determines the locator identification strategy to be used to
# validate if the current locator is available in DOM. It creates an object to store all the locators
# in LocatorStore as well as all the alternate locators.


class LocatorInfo:

    # Constructor for LocatorInfo used to store locators.
    def __init__(self, locator_id=None, parent_id=None, strategy=None, locator=None):
        self.locator_id = locator_id
        self.parent_id = parent_id
        self.strategy = strategy
        self.locator = locator

    # Method:       process_locator
    # Type:         Class
    # Description:  Processes the current locator passed in *** Get Heal Locator *** keyword and creates a LocatorInfo
    #               object to help evaluate the presence of the element in DOM and subsequently compare the presence of
    #               Locator in Element Information file and evaluating the alternate locator strategies if it is not
    #               available.
    @classmethod
    def process_locator(cls, locator):
        # Sets the locator check to process and analyze the input format of the locator
        locator_check = [':', '=']

        for format_check in locator_check:
            if locator.find(format_check) != -1:
                # Parsing and analyzing the current strategy used through delimiters.
                strategy = locator[0: locator.find(format_check)].strip()
                discreet_strategy = Strategy.get_Strategy_Type(strategy)
                if not discreet_strategy:
                    continue
                else:
                    # Analyzing the locator and creating the LocatorInfo object
                    locator = locator[locator.find(format_check) + 1:]
                    locator_info = cls(strategy=discreet_strategy, locator=locator)
                    break
                pass
            pass

        if not discreet_strategy:
            # Creating the LocatorInfo object by using the default locator strategy as xpath
            # and locator initialized to literal.
            locator_info = cls(strategy=Strategy.xpath, locator=locator)
            pass
        return locator_info

    # Getters and setters

    # Sets the current Locator or Alternate Locator id
    def set_locator_id(self, locator_id):
        self.locator_id = locator_id

    # Sets the parent id of the current locator. The parent can be a page for locator tag and a locator for alt tag.
    def set_parent_id(self, parent_id):
        self.parent_id = parent_id

    # Sets the identification strategy of the locator
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Sets the Locator literal
    def set_locator(self, locator):
        self.locator = locator

    # Gets the locator id of the Locator Info object.
    def get_locator_id(self):
        return self.locator_id

    # Gets the parent id of the Locator Info object.
    # The parent could be a page for locator tag or locator for alt tag.
    def get_parent_id(self):
        return self.parent_id

    # Gets the locator strategy used to identify the element.
    def get_strategy(self):
        return self.strategy

    # Gets the locator literal
    def get_locator(self):
        return self.locator

    # String representation of Locator Info
    def __repr__(self):
        return 'LocatorInfo(locator_id: "' + \
               self.page_id + "', parent_id: " + \
               self.parent_id + "strategy:" + \
               self.strategy + "', locator: " + \
               self.locator + "')"
