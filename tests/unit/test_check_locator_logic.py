import pytest
from utils.BasePage import BasePage
from locatores.locator import Locator
from locatores.strategies import LocateBy

class Test_check_locator_logic():
    
    @pytest.mark.unit
    def test_check_locator_logic_success(self,page):

        login_button = Locator(
        by=LocateBy.TEXT,
        value="password",
        )
        base_page=BasePage(page)
        base_page._locate_element(login_button)
    
    @pytest.mark.unit
    def test_check_locator_logic_name_missing(self,page):
        
        login_button = Locator(
        by=LocateBy.ROLE,
        value="password",
        )
        base_page=BasePage(page)
        base_page._locate_element(login_button)
    
    @pytest.mark.unit
    def test_check_locator_logic_failed(self,page):

        login_button = Locator(
        by=LocateBy.Test,
        value="password",
        )

        base_page=BasePage(page)
        base_page._locate_element(login_button)
