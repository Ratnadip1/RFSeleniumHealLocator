import enum

"""
Strategy is an enumerator that is used to list the different strategies and switchers to operate and evaluate 
locators and create alternate locators.
"""


class Strategy(enum.Enum):

    # 'id' is used for 'id' locator strategy.
    id = 1

    # 'name' is used for 'name' locator strategy.
    name = 2

    # 'xpath' is used for 'xpath' locator strategy.
    xpath = 3

    # 'cssSelector' is used for 'css selector' locator strategy.
    cssSelector = 4

    # 'cls' is used from 'class' locator strategy.
    cls = 5

    # 'linkText' is used for 'linkText' locator strategy.
    linkText = 6

    # 'linkText' is used for 'linkText' locator strategy.
    tagName = 7

    pass
