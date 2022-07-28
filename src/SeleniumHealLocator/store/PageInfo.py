
"""
Class:          PageInfo
Description:    Data Container class to store information about individual pages.
Attributes:     page_id, page_base_url, page_path, page_scope
"""


class PageInfo(object):

    # Constructor for PageInfo objects
    def __init__(self, page_id=None, page_base_url=None, page_path=None, page_scope=None):
        self.page_id = page_id
        self.page_base_url = page_base_url
        self.page_path = page_path
        self.page_scope = page_scope
        pass

    # Getters and setters
    def get_Page_Id(self):
        return self.page_id

    def get_Page_Base_Url(self):
        return self.page_base_url

    def get_Page_Path(self):
        return self.page_path

    def get_Page_Scope(self):
        return self.page_scope

    def set_Page_Base_Url(self, page_base_url):
        self.page_base_url = page_base_url

    def set_Page_Path(self, page_path):
        self.page_path = page_path

    def set_Page_Scope(self, page_scope):
        self.page_scope = page_scope

    # String representation of PageInfo object.
    def __repr__(self):
        return 'PageInfo: base_url-> ' \
               + self.page_base_url + ', path-> ' \
               + self.page_path + ', scope -> ' \
               + self.page_scope
