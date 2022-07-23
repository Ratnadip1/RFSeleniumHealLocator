from src.SeleniumHealLocator import SeleniumHealLocator
from robot.libraries.BuiltIn import RobotNotRunningError


def test_Selenium_Library():
    try:
        SeleniumHealLocator()
    except Exception as ex:
        assert RobotNotRunningError, ex
