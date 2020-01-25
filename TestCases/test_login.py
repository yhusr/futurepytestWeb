"""
Time:2020/1/12 0012
"""
import time
import pytest
from ddt import ddt,data
from PageObjects.home_page import HomePage
from TestData.common_data import WebCommon as WM
from TestData.login_case_data import LoginData
from PageObjects.login_page import LoginPageTest


@pytest.mark.master
@pytest.mark.usefixtures('set_up')
class TestLogin:

    # 登录的正向用例
    def test_login_1_success(self, set_up):
        LoginPageTest(set_up).my_login(LoginData.right_data['username'], LoginData.right_data['password'])
        time.sleep(2)
        actual_url = set_up.current_url
        assert WM.index_url == actual_url
        assert HomePage.my_account_exist()

    # 登录的反向用例
    @pytest.mark.parametrize('my_data', LoginData.error_data)
    def test_login_0_error(self, set_up, my_data):
        LoginPageTest(set_up).my_login(my_data['username'], my_data['password'])
        time.sleep(2)
        actual_url = set_up.current_url
        assert WM.login_url == actual_url
        assert LoginPageTest(set_up).login_error_text() == my_data['value']
