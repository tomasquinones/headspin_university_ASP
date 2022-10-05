from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView


class HomeView(BaseView):
    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, "Echo Box")

    def nav_to_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
