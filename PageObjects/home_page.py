"""
Time:2020/1/12 0012
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from CommonHandle.basepage import BasePage as BP
from PageLocaltors.home_page_loc import HomePage as loc


class HomePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    @staticmethod
    def my_account_exist():
        """
        判断登录是否成功，我的账户字样是否显示
        :return: 显示字样返回真，不显示字样返回假
        """
        account_exist_loc = (By.XPATH, '//a[contains(text(),"我的帐户")]')
        if account_exist_loc:
            return True
        else:
            return False

    # 点击第一个抢投标按钮,进入投标界面
    def first_ele_click(self):
        BP(self.driver).click_ele(loc.my_bid_loc, photo_screen='登录成功后_点击页面第一个抢投标')


