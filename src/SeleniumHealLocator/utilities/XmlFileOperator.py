import os
import threading
from xml.dom import minidom

from ..utilities.ElementInformation import ElementInformation
from ..exceptions.HealLocatorException import HealLocatorException

"""
XmlFileOperator is used to implement the construction of 'XML' based Element Information file.
The class includes generation of XML file and writing all the element information on test closure.
Processing and retrieving information from Element Information file is also implemented.
"""


class XmlFileOperator(ElementInformation):

    _lock = None

    def __init__(self):
        super()
        XmlFileOperator._lock = threading.Lock()

    # Construct the file name as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_File(self, file_name):
        try:
            if not file_name.endswith(".xml"):
                file_name = file_name.__add__(".xml")

            self.file_name = file_name
            pass
        except HealLocatorException as ex:
            print(ex.with_traceback())
            pass

    # Generates the XML file for the first time if it is not already available.
    # It is a one-time activity and creates all the required
    def generate_Element_Information(self):
        super().generate_Element_Information()
        try:
            with XmlFileOperator._lock:
                root = minidom.Document()

                xml = root.createElement('elements')
                root.appendChild(xml)

                xml_str = root.toprettyxml(indent="\t")

                save_path_file = self.folder_location + os.sep + self.file_name

                with open(save_path_file, "w") as f:
                    f.write(xml_str)
        except HealLocatorException as exception:
            print(exception.with_traceback())
            pass

    pass
