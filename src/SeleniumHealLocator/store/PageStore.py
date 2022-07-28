import threading

from .PageInfo import PageInfo
from .. import ManageInformation
from ..utilities.HealLog import HealLog

"""
PageStore class stores the information of all the pages explored during the test run and 
saves them in the Element Information file. On initiation, it checks the available listed page nodes
in Element Information file. On invoking the keyword *** Get Heal Locator ***, it checks if information
of the current page for the targeted locator is available in PageStore. If the same is not available, the 
current page information is constructed and added to the PageStore list.
"""


class PageStore(object):

    __lock = threading.Lock()
    __pageStoreInstance = None

    # Constructor for PageStore object. Setup of the Page Store process.
    # Initiates the page store dictionary with existing Element Information file data.
    # Initiates the index based on existing data in ElementInfo value.
    def __init__(self):
        self.pageStoreDict = {}
        self.elementInfo = ManageInformation.get_Instance().get_Element_Info()
        self.populate_page_Store_Dict()
        self.page_id = len(self.pageStoreDict) + 1
        self.logger = HealLog()
        pass

    # Method:       get_Instance
    # Type:         Class
    # Description:  Singleton implementation of PageStore class
    # Returns:      Singleton instance
    @classmethod
    def get_Instance(cls):
        if not cls.__pageStoreInstance:
            with cls.__lock:
                if not cls.__pageStoreInstance:
                    cls.__pageStoreInstance = cls()
                    pass
        return cls.__pageStoreInstance

    def get_Page_Info(self, url):
        # Initializing local variables.
        base_url = None
        path = None
        page_scope = None

        # Remove http_scope from baseUrl
        if url.startswith("http"):
            page_scope = url[0: url.index("://") + 3]
            url = url[url.index("://") + 3:]

        # Remove query & separators from baseUrl
        url = self.format_page_url(url)

        # Parsing the base url and path
        if url.find("/") != -1:
            base_url = url[0:url.index("/")]
            path = url[url.index("/"):]

        # Validates if the page is already listed in the Element Information file.
        # If the PageInfo is already available in the Element Information file,
        # it would return the corresponding page id of the PageInfo instance listed in dictionary.
        page_id = self.is_page_listed(base_url, path, page_scope)

        # If the Page information for the current browser page is not listed in the PageStore
        # dictionary, a PageInfo object with current Page information will be created and stored.
        if page_id is None:
            page = PageInfo(page_id=self.page_id, page_base_url=base_url, page_path=path, page_scope=page_scope)
            self.logger.info('Page information is not available in Page Store: ' + str(page))
            self.pageStoreDict[str(self.page_id)] = page
            page_id = self.page_id
            self.page_id += 1
        else:
            self.logger.info('Page information is already available in Page Store: ' +
                             str(base_url) + ' ' + str(path) + ' ' + str(page_scope))
        return page_id

    # Static method for formatting the url to store the value in PageInfo object.
    @staticmethod
    def format_page_url(url):
        if url.find("?") != -1:
            url = url[0: url.index("?")]
        if url.find("#") != -1:
            url = url[0: url.index("#")]
        return url

    # Method: is_page_listed
    # Compares the PageInfo and retrieves the Index in dictionary if the entry is available
    # or returns null.
    def is_page_listed(self, base_url, path, page_scope):
        dict_items = self.pageStoreDict.items()
        filtered_dict = dict(filter(lambda e: e[1].get_Page_Base_Url() == base_url
                                              and e[1].get_Page_Path() == path
                                              and e[1].get_Page_Scope() == page_scope,
                                    dict_items))
        if len(filtered_dict.keys()) == 0:
            return None
        else:
            return list(filtered_dict.keys())[0]

    # Retrieves the list of PageInfo from Element Information file and stores it in PageInfo.
    def populate_page_Store_Dict(self):
        page_list = self.elementInfo.getPageList()
        for page in page_list:
            self.pageStoreDict[str(page.get_Page_Id())] = page
        pass
