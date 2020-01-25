"""
Time:2020/1/23 0023
"""
from selenium.webdriver.common.by import By


class UserPage:
    # 可用余额
    surplus_available = (By.XPATH, '//li[@class="color_sub"]')
