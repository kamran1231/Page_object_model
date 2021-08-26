from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillForm(self, name, phoneNum, email, country, city, username, password):
        self.type("name_XPATH",name)
        self.type("phone_XPATH",phoneNum)
        self.type("email_XPATH",email)
        self.select("country_XPATH",country)
        self.type("city_XPATH",city)
        self.type("username_XPATH",username)
        self.type("password_XPATH",password)
        self.click("submit_XPATH")
