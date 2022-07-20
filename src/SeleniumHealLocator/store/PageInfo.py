
"""
Class: PageInfo
Description:
"""


class PageInfo(object):

    def __init__(self, page_base_url=None, page_path=None, page_scope=None):
        self.page_base_url = page_base_url
        self.page_path = page_path
        self.page_scope = page_scope
        pass

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

    def __repr__(self):
        return 'PageInfo: base_url-> ' \
               + self.page_base_url + ', path-> ' \
               + self.page_path + ', scope -> ' \
               + self.page_scope
