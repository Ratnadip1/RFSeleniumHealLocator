from src.SeleniumHealLocator import SeleniumHealLocator


def test_Selenium_Library():
    try:
        SeleniumHealLocator()
    except Exception as ex:
        assert 'RobotNotRunningError', ex.__cause__
