"""
Time:2020/1/25 0025
"""
import time
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPageTest
from TestData.common_data import WebCommon as WM
from PageObjects.classroom_page import ClassRoomPage as CR


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()
    driver.get(WM.login_url)
    # lp = LoginPageTest(driver)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture()
# def my_setup(set_up):
#     LoginPageTest(set_up).my_login(WM.username, WM.password)
#     bp = CR(set_up)
#     yield set_up, bp
#     set_up.quit()


# @pytest.fixture()
# def letter():
#     driver = webdriver.Chrome()
#     driver.get(WM.login_url)
#     driver.maximize_window()
#     LoginPageTest(driver).my_login(WM.username, WM.password)
#     time.sleep(2)
#     CR(driver).info_ele_click()
#     yield driver
#     driver.quit()
