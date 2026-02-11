import pytest
from playwright.sync_api import sync_playwright

from network_utils.api_recorder import APIRecorder

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False,slow_mo=1000)

        yield browser

        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()    

    yield page

    context.close() 

@pytest.fixture
def api_recorder(page):
    api_recorder=APIRecorder(page)
    
    api_recorder.start_recorder()
    
    yield api_recorder

    api_recorder.stop_recorder()