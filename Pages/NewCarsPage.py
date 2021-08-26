from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.click("Bmw_XPATH")

    def selectHonda(self):
        self.click("honda_XPATH")
