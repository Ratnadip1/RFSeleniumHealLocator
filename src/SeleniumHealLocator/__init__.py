from robotlibcore import DynamicCore
from .keywords.ManageInformation import ManageInformation
from .keywords.HealElement import HealElement

"""
SeleniumHealLocator facilitates the Robot Framework by introducing the Keyword libraries.
Listing the libraries containing keywords and setting the Dynamic Core libraries field with the keyword module
classes exposes the keywords to Robot Framework and hence is used seamlessly.
"""


class SeleniumHealLocator(DynamicCore):
    info_type = None

    def __init__(self):
        # Listing the libraries with Keywords to be used by Robot Framework
        libraries = [
            ManageInformation.get_Instance(),
            HealElement()
        ]

        # Invoking the DynamicCore superclass constructor with listed keyword library modules.
        DynamicCore.__init__(self, libraries)
