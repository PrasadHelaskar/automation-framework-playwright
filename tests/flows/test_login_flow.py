import pytest

from pages.login_page import LoginPage
from utils.logger import Logger

log= Logger().get_logger(__name__)

class TestLoginFlow():
    @pytest.mark.flows
    def test_login_flow(self,page,api_recorder):
        login_page=LoginPage(page)
        page.goto("https://www.saucedemo.com/")
        login_page.type_username("standard_user")
        login_page.type_password("secret_sauce")
        login_page.click_submit()

        apis=api_recorder.get_records()

        for api in apis:
            log.info("Url: %s", api["url"])

        log.info("Login flow execution completed")