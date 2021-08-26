from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def doLogin(self):
        pass