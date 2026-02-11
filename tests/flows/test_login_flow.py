import os
import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from utils.logger import Logger

log= Logger().get_logger(__name__)

class TestLoginFlow():
    @pytest.mark.flows
    def test_login_flow(self,page,api_recorder):
        load_dotenv(".config/.env")
        login_page=LoginPage(page)
        page.goto(os.getenv("URL"))
        login_page.type_username(os.getenv("USERNAME"))
        login_page.type_password(os.getenv("PASSWORD"))
        login_page.click_submit()

        apis=api_recorder.get_records()

        for api in apis:
            log.info("Url: %s", api["url"])

        log.info("Login flow execution completed")