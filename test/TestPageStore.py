from src.SeleniumHealLocator.store.PageStore import PageStore
from src.SeleniumHealLocator.keywords.ManageInformation import ManageInformation


def test_PageStore_getPageInfo_first_data():
    manage_information = ManageInformation.get_Instance()
    manage_information.initiate_Healing_Process(folder_location='Test', file_name='TestPageStore', file_type='.xml')
    page_store = PageStore.get_Instance()
    # .get_Instance()
    assert page_store, isinstance(page_store, PageStore.__class__)
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=k")
    print(page_id)
    assert 2 == page_id


def test_PageStore_getPageInfo_duplicate_data():
    page_store = PageStore.get_Instance()
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=p")
    print(page_id)
    assert 2 == page_id


def test_PageStore_getPageInfo_second_data():
    # assert page_store, isinstance(page_store, PageStore.__class__)
    page_store = PageStore.get_Instance()
    page_id = page_store.get_Page_Info("https://www.google.com/Mail#accounts")
    print(page_id)
    assert 3 == page_id


def test_PageStore_getPageInfo_Keys():
    page_store = PageStore.get_Instance()
    ctr = 1
    for key in page_store.pageStoreDict.keys():
        assert key == ctr
        ctr += 1

