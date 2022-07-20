from src.SeleniumHealLocator.store.PageStore import PageStore


def test_PageStore_getPageInfo():
    page_store = PageStore()
    # .get_Instance()
    assert page_store, isinstance(page_store, PageStore.__class__)
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=k")
    assert 1, page_id
    page_id = page_store.get_Page_Info("https://www.google.com/Accounts?q=p")
    assert 1, page_id
    assert page_store, isinstance(page_store, PageStore.__class__)
    page_id = page_store.get_Page_Info("https://www.google.com/Mail#accounts")
    assert 2, page_id

