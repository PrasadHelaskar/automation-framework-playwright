from locatores.locator import Locator
from locatores.strategies import LocateBy
from utils.BasePage import BasePage
from utils.logger import Logger

log=Logger().get_logger(__name__)


class LoginPage(BasePage):
    _private_username=Locator(
        by=LocateBy.PLACEHOLDER,
        value="Username"        
    )

    _private_password=Locator(
        by=LocateBy.PLACEHOLDER,
        value="Password"
    )

    _private_submit_button=Locator(
        by=LocateBy.CSS,
        value="input[id='login-button']"
    )

    def type_username(self,username:str):
        self.type(self._private_username,username)
    
    def type_password(self,password:str):
        self.type(self._private_password,password)

    def click_submit(self):
        self.click(self._private_submit_button)