from src.SeleniumHealLocator.store.LocatorInfo import LocatorInfo
from src.SeleniumHealLocator.evaluation.Strategy import Strategy


def test_Process_Locator_Colon():
    locator_info_instance = LocatorInfo.process_locator('id:q')
    assert locator_info_instance.get_locator() == 'q'
    assert locator_info_instance.get_strategy() == Strategy.id
    pass


def test_Process_Locator_Equal():
    locator_info_instance = LocatorInfo.process_locator('name=btnK')
    assert locator_info_instance.get_locator() == 'btnK'
    assert locator_info_instance.get_strategy() == Strategy.name
    pass


def test_Process_Locator_XPath():
    locator_info_instance = LocatorInfo.process_locator('//button[@name="btnK"]')
    assert locator_info_instance.get_locator() == '//button[@name="btnK"]'
    assert locator_info_instance.get_strategy() == Strategy.xpath
    pass
