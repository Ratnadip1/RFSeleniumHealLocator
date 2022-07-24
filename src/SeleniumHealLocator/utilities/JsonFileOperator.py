import os
import threading
import json

from ..utilities.ElementInformation import ElementInformation
from ..exceptions.HealLocatorException import HealLocatorException

"""
JsonFileOperator is used to implement the construction of 'Json' based Element Information file.
The class includes generation of XML file and writing all the element information on test closure.
Processing and retrieving information from Element Information file is also implemented.
"""


class JsonFileOperator(ElementInformation):

    _lock = None

    def __init__(self):
        super()
        JsonFileOperator._lock = threading.Lock()

    # Construct the file name as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_File(self, file_name):
        try:
            if not file_name.endswith(".json"):
                file_name = file_name.__add__(".json")

            self.file_name = file_name
            pass
        except HealLocatorException as ex:
            self.logger.error(ex)
            pass

    # Generates the XML file for the first time if it is not already available.
    # It is a one-time activity and creates all the required
    def generate_Element_Information(self):
        super().generate_Element_Information()
        try:
            with JsonFileOperator._lock:
                # Constructing the blank Json with elements Json Array
                element_json = {"elements": {}}

                # Constructing the path where Json file will be saved
                save_path_file = self.folder_location + os.sep + self.file_name

                # Write the startup json content into the newly generated Element Information file in .json format
                with open(save_path_file, 'a') as jsonFile:
                    json.dump(element_json, jsonFile, ensure_ascii=False, indent=4)
                pass

        except Exception as ex:
            raise HealLocatorException('Error occurred while generating Element Information file in .json format.')
            pass

    pass
