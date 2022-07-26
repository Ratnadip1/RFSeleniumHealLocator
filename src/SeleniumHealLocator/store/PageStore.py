import threading

from .PageInfo import PageInfo
from .. import ManageInformation

"""
PageStore class stores the information of all the pages explored during the test run and 
saves them in the Element Information file.
"""


class PageStore(object):

    __lock = threading.Lock()
    __pageStoreInstance = None

    def __init__(self):
        self.pageStoreDict = {}
        self.elementInfo = ManageInformation.get_Instance().get_Element_Info()
        self.populate_page_Store_Dict()
        self.page_id = len(self.pageStoreDict) + 1
        pass

    @classmethod
    def get_Instance(cls):
        if not cls.__pageStoreInstance:
            with cls.__lock:
                if not cls.__pageStoreInstance:
                    cls.__pageStoreInstance = cls()
                    pass
        return cls.__pageStoreInstance

    def get_Page_Info(self, url):
        # Remove http_scope from baseUrl
        base_url = None
        path = None
        page_scope = None

        if url.startswith("http"):
            page_scope = url[0: url.index("://") + 3]
            url = url[url.index("://") + 3:]

        # Remove query & separators from baseUrl
        url = self.format_page_url(url)

        # Parsing the base url and path
        if url.find("/") != -1:
            base_url = url[0:url.index("/")]
            path = url[url.index("/"):]

        page_id = self.is_page_listed(base_url, path, page_scope)

        if page_id is None:
            page = PageInfo(page_id=self.page_id, page_base_url=base_url, page_path=path, page_scope=page_scope)
            print('Page information is not available in Page Store: ' + str(page))
            self.pageStoreDict[str(self.page_id)] = page
            page_id = self.page_id
            self.page_id += 1
            pass
        else:
            print('Page information is already available in Page Store: '
                  + str(base_url) + ' ' + str(path) + ' ' + str(page_scope))
        return page_id
        pass

    @staticmethod
    def format_page_url(url):
        if url.find("?") != -1:
            url = url[0: url.index("?")]
        if url.find("#") != -1:
            url = url[0: url.index("#")]
        return url

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

    def populate_page_Store_Dict(self):

        page_list = self.elementInfo.getPageList()
        for page in page_list:
            self.pageStoreDict[str(page.get_Page_Id())] = page
        pass
