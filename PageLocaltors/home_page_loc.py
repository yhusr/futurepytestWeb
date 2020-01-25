"""
Time:2020/1/22 0022
"""
from selenium.webdriver.common.by import By


class HomePage:
    # 抢投标按钮
    my_bid_loc = (By.XPATH, '//a[text()="抢投标"]')