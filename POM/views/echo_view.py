from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView


class EchoView(BaseView):
    MESSAGE_INPUT = (MobileBy.ACCESSIBILITY_ID, "messageInput")
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, "messageSaveBtn")
    MESSAGE_LABEL = (MobileBy.ACCESSIBILITY_ID, "savedMessage")

    def save_message(self, message):
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.find(self.SAVE_BUTTON).click()

    def read_message(self):
        return self.find(self.MESSAGE_LABEL).text

    def nav_back(self):
        self.driver.back()
