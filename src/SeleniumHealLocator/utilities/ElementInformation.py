import os
import threading
from os import path

"""
Element Information is the base class that handles the file operations of the Element Information
File used to store the alternate locator strategies, locator and page information of the WebElement
that are called in the *** Get Heal Locator *** keyword.
"""


class ElementInformation(object):

    _lock = None
    # Constructor for ElementInformation object.
    # Parameters:   folder_location, file_name
    # Description:  Initializes the essential variables for usage in Implementation classes and
    #               common methods.

    def __init__(self):
        self.folder_location = None
        self.file_name = None
        ElementInformation._lock = threading.Lock()
        pass

    # Construct the folder location as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_Folder(self, folder_location):
        with self._lock:
            if not folder_location:
                folder_location = os.getcwd() + os.sep
            else:
                folder_location = os.getcwd() + os.sep + folder_location
            self.folder_location = folder_location
            pass

    """
    Method:         infoExists
    Type:           Instance
    Description:    Validates the folder structure and availability of element information
                    file is already generated. Returns a flag based on the availability of
                    element information file
    Returns:        boolean value
    """

    def info_Exists(self):
        return path.exists(self.folder_location + os.sep + self.file_name)

    """
    Function:       generate_Element_Information
    Type:           Instance
    Description:    Generates the Element Information folder and passes on to 
    the subclasses for further implementation.
    """

    def generate_Element_Information(self):
        with ElementInformation._lock:
            if not path.exists(self.folder_location):
                os.makedirs(self.folder_location)

