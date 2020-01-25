"""
Time:2020/1/23 0023
"""
from selenium.webdriver.remote.webdriver import WebDriver
from PageLocaltors.user_page_loc import UserPage as loc
from CommonHandle.basepage import BasePage as BP


class UserPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 获取剩余的可用资金
    def get_my_account(self):
        """
        返回剩余可用资金
        :return:
        """
        my_account = BP(self.driver).get_text(loc.surplus_available, '个人中心_获取可用的剩余资金')
        account = my_account.strip('元')
        return account