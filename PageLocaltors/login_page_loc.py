"""
Time:2020/1/15 0015
"""
from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 登录页面用户名的定位
    username_loc = (By.NAME, 'phone')
    # 登录页面密码的定位
    password_loc = (By.NAME, 'password')
    # 登录页面登录按钮的定位
    login_button_loc = (By.XPATH, '//button[text()="登录"]')
    # 登录页面输入为空输入框的错误提示
    login_error_loc = (By.XPATH, '//div[@class="form-error-info"]')