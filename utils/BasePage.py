from utils.logger import Logger
from locatores.locator import Locator

log=Logger().get_logger(__name__)

class BasePage:
    def __init__(self,page):
        self.page=page

    def _locate_element(self, locator: Locator):
        return locator.resolve(self.page)

    def click(self,locator):
        self._locate_element(locator).click()

    def type(self,locator,data):
        self._locate_element(locator).fill(data)

    def assert_title(self, title: str):
        current_title=self.page.title()
        assert current_title == title
        return current_title
