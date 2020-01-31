"""
Time:2020/1/30 0030
"""
import pytest
import time
from selenium import webdriver
from PageObjects.login_page import LoginPageTest
from TestData.common_data import WebCommon as WM
from PageObjects.classroom_page import ClassRoomPage as CR
from PageObjects.homework_page import HomeWorkPage
from TestData.homework_case_data import HomeWorkCase


@pytest.fixture()
def home_fre():
    driver = webdriver.Chrome()
    driver.get(WM.login_url)
    driver.maximize_window()
    LoginPageTest(driver).my_login(WM.username, WM.password)
    time.sleep(2)
    CR(driver).info_ele_click()
    yield driver
    driver.execute_script('window.location.href="'+WM.index_url+'"')
    CR(driver).drop_course(password=WM.password)
    driver.quit()


@pytest.mark.master
@pytest.mark.mytest
@pytest.mark.usefixtures('home_fre')
class TestHomeWork:
    # 作业文件上传用例
    def test_homework_upload(self, home_fre):
        success_text = HomeWorkPage(home_fre).homework_upload_submit(path=HomeWorkCase.filepath)
        assert HomeWorkCase.success_data['homework_submit'] == success_text

    # 作业留言用例
    def test_homework_message(self, home_fre):
        message_text = HomeWorkPage(home_fre).homework_message(content=HomeWorkCase.success_data['message'])
        assert HomeWorkCase.success_data['message'] == message_text