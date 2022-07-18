from src.SeleniumHealLocator.utilities.ElementInformation import ElementInformation
from robot.api.deco import keyword


class ManageInformation(object):
    """
            Keyword: ***Initiate Heal Locator***
            Starts off with the Robot Framework - Selenium WebElement Heal Process.
            Validates if the Element Information file is already available.
            Generates new Element Information File - if there is no existing data.
        """

    def __init__(self):
        self.element_info = None
        pass

    @keyword
    def initiate_Healing_Process(self, folder_location, file_name="elements"):
        # Constructs the element information file

        self.element_info = ElementInformation(folder_location, file_name)

        if self.element_info.info_Exists():
            print("Element Information File {} already exists in Location {}.".format(file_name, folder_location))
        else:
            self.element_info.generate_Element_Information()
            print("Element Information file generated...")

        pass

    pass
