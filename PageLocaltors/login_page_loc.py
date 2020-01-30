"""
Time:2020/1/15 0015
"""
from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 登录页面用户名的定位
    username_loc = (By.NAME, 'account')
    # 登录页面密码的定位
    password_loc = (By.NAME, 'pass')
    # 登录页面登录按钮的定位
    login_button_loc = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
    # 登录失败的错误文本显示
    error_login_text_loc = (By.XPATH, '//a[@class="active"]')
