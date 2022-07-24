from . import ElementInformation
# from ..keywords.ManageInformation import ManageInformation
from ..utilities.XmlFileOperator import XmlFileOperator
from ..utilities.JsonFileOperator import JsonFileOperator


class FileOperatorSwitcher:

    @staticmethod
    def get_File_Operator(file_type):
        switcher = {
            '.xml': XmlFileOperator(),
            '.json': JsonFileOperator()
        }
        return switcher.get(file_type, None)
