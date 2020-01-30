"""
Time:2020/1/12 0012
"""
from selenium.webdriver.remote.webdriver import WebDriver
from PageLocaltors.login_page_loc import LoginPageLoc as loc
from CommonHandle.basepage import BasePage as BP


# 登录页面的元素操作
class LoginPageTest:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 页面操作方法
    def my_login(self, username, password):
        """
        进行登录的操作
        :param username: 输入的用户名
        :param password: 输入的密码
        :return:
        """
        # 用户框中输入用户名
        BP(self.driver).input_content(loc.username_loc, photo_screen='登录页面_用户名输入', content=username)
        # 密码框中输入密码
        BP(self.driver).input_content(loc.password_loc, photo_screen='登录页面_密码输入', content=password)
        # 点击登录按钮进入页面
        BP(self.driver).click_ele(loc.login_button_loc, photo_screen='登录页面输入完成_点击登录按钮')

    # 登录错误的文本显示
    def login_error_text(self):
        return BP(self.driver).get_text(loc.error_login_text_loc, photo_screen='登录失败后，页面文本显示')