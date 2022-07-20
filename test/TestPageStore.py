from src.SeleniumHealLocator.store.PageStore import PageStore


def test_PageStore_getPageInfo_first_data():
    page_store = PageStore.get_Instance()
    # .get_Instance()
    assert page_store, isinstance(page_store, PageStore.__class__)
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=k")
    print(page_id)
    assert 1, page_id


def test_PageStore_getPageInfo_duplicate_data():
    page_store = PageStore.get_Instance()
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=p")
    print(page_id)
    assert 1, page_id


def test_PageStore_getPageInfo_second_data():
    # assert page_store, isinstance(page_store, PageStore.__class__)
    page_store = PageStore.get_Instance()
    page_id = page_store.get_Page_Info("https://www.google.com/Mail#accounts")
    print(page_id)
    assert 2, page_id
