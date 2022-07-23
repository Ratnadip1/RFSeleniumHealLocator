from ..exceptions.HealLocatorException import HealLocatorException
from ..utilities import FileOperatorSwitcher
from robot.api.deco import keyword
from robot.output.logger import Logger


class ManageInformation(object):

    def __init__(self):
        self.element_info = None
        self.logger = Logger()
        pass

    """
            Keyword: ***Initiate Healing Process***
            Starts off with the Robot Framework - Selenium WebElement Heal Process.
            Validates if the Element Information file is already available.
            Generates new Element Information File - if there is no existing data.
            Optional parameter file_type is '.xml' by default. file_type parameter will be provisioned to 
            accept '.json' format.
            Based on the file_type specified, the Element information file will be created in the given format 
    """

    @keyword
    def initiate_Healing_Process(self, folder_location, file_name="elements", file_type=".xml"):
        # Constructs the element information file

        # Instantiate ElementInformation and provide folder and
        # file name for tracking the element information.
        try:
            # Retrieves the format of Element Information File to be generated
            self.element_info = FileOperatorSwitcher.get_File_Operator(file_type)
            if not self.element_info:
                # An exception is raised if the Element Information File format is unsupported and ElementInformation is
                # not assigned to relevant file operator.
                raise HealLocatorException('Unsupported file_type selected. Supports only ".xml" and ".json" format')
                pass
            else:
                self.element_info.set_Test_Element_Snapshot_Folder(folder_location)
                self.element_info.set_Test_Element_Snapshot_File(file_name)

                # Validates if the Element Information file is already in place. If not,
                # generates an Element Information file with a root element.
                if self.element_info.info_Exists():
                    self.logger.message("Element Information File {} already exists in Location {}.".format(file_name, folder_location))
                else:
                    self.element_info.generate_Element_Information()
                    self.logger.message("Element Information file generated...")
        except HealLocatorException as exception:
            self.logger.error(exception.with_traceback())
            pass
