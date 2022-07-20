import os
from os import path
from xml.dom import minidom

"""
Element Information handles the file operations of the Element Information File used to store
the 
"""


class ElementInformation(object):

    is_Element_Information_Initiated_Flag = False

    # Constructor for ElementInformation object.
    # Parameters:   folder_location, file_name
    # Description:  Initializes the essential variables for
    def __init__(self):
        self.folder_location = None
        self.file_name = None
        pass

    # Construct the folder location as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_Folder(self, folder_location):
        if folder_location is not None:
            folder_location = os.getcwd() + os.sep + folder_location
            self.folder_location = folder_location

    # Construct the file name as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_File(self, file_name):
        if file_name is not None:
            if not file_name.endswith(".xml"):
                file_name = file_name.__add__(".xml")
            self.file_name = file_name
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
    Description:    Generates the Element Information file 
    """

    def generate_Element_Information(self):

        if not path.exists(self.folder_location):
            os.makedirs(self.folder_location)

        root = minidom.Document()

        xml = root.createElement('elements')
        root.appendChild(xml)

        xml_str = root.toprettyxml(indent="\t")

        save_path_file = self.folder_location + os.sep + self.file_name

        with open(save_path_file, "w") as f:
            f.write(xml_str)
