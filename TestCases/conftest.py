"""
Time:2020/1/25 0025
"""
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPageTest
from TestData.common_data import WebCommon as WM
from PageObjects.home_page import HomePage as HP
from PageObjects.bid_page import BidPage as BP


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()
    driver.get(WM.login_url)
    # lp = LoginPageTest(driver)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def my_setup(set_up):
    LoginPageTest(set_up).my_login(WM.username, WM.password)
    bp = BP(set_up)
    hp = HP(set_up)
    yield set_up, bp, hp
    set_up.quit()
