import os
import threading
from xml.dom import minidom
import xml.etree.ElementTree as ET

from ..utilities.ElementInformation import ElementInformation
from ..exceptions.HealLocatorException import HealLocatorException
from ..store.PageInfo import PageInfo

"""
XmlFileOperator is used to implement the construction of 'XML' based Element Information file.
The class includes generation of XML file and writing all the element information on test closure.
Processing and retrieving information from Element Information file is also implemented.
"""


class XmlFileOperator(ElementInformation):

    def __init__(self):
        super().__init__()
        ElementInformation._lock = threading.Lock()

    # Construct the file name as provided by the argument in
    # 'Initiate Healing Process' keywords in Robot Framework
    def set_Test_Element_Snapshot_File(self, file_name):
        try:
            if not file_name.endswith(".xml"):
                file_name = file_name.__add__(".xml")

            self.file_name = file_name
            pass
        except Exception:
            raise HealLocatorException('Error occurred while constructing Element Information File Name')
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
        except Exception:
            raise HealLocatorException('Error occurred while generating Element Information file in .xml format')
            pass

    # Method:       get_Page_List
    # Type:         Instance
    # Description:  Retrieves the list of pages available in Element Information File.
    #               The implementation in the given method is for .xml file type
    # Returns:      List of PageInfo parsed from Element Information file.
    def get_Page_List(self):
        page_list = []
        tree = ET.parse(self.folder_location + os.sep + self.file_name)
        root = tree.getroot()
        for pageItem in root.findall('.//page'):
            page_entry = PageInfo(page_id=pageItem.attrib['id'])
            page_entry.set_Page_Scope(page_scope=pageItem.attrib['scope'])
            page_entry.set_Page_Base_Url(page_base_url=pageItem.attrib['baseUrl'])
            page_entry.set_Page_Path(page_path=pageItem.attrib['path'])
            page_list.append(page_entry)
        return page_list

    pass
