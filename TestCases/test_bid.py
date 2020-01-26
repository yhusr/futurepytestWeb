"""
Time:2020/1/22 0022
"""
import time
import pytest
from TestData.bid_case_data import BidCase as BC

# @pytest.fixture(params=BC.fail)
# def my_params(request):
#     return request.param


@pytest.mark.master
@pytest.mark.usefixtures('my_setup')
class TestBid:
    # 正向投标用例

    def test_bid_page(self, my_setup):
        my_setup[2].first_ele_click()
        time.sleep(2)
        # 获取投标前的数据
        invest_forward_user = float(my_setup[1].get_user_data())
        invest_forward_account = float(my_setup[1].get_bid_surplus())
        # 开始投标
        my_setup[1].input_bid(BC.success['invest_data'])
        my_setup[1].bid_button_click()
        my_setup[1].active_button_click()
        # 返回上一页获取数据
        my_setup[0].back()
        my_setup[0].refresh()
        # 重新获取投标前的用户可用资金
        invest_forward_user_back = float(my_setup[1].get_user_data())
        invest_forward_account_back = float(my_setup[1].get_bid_surplus())
        # 断言用户资金变化和可投资金额的变化
        assert invest_forward_user-invest_forward_user_back == BC.success['invest_data']
        assert invest_forward_account-invest_forward_account_back, BC.success['invest_data']/10000

    # 反向投标用例
    # @data(*BC.fail)
    # @pytest.mark.usefixtures('my_params')
    # def test_bid_page_fail(self, my_setup, my_params):
    #     my_setup[2].first_ele_click()
    #     time.sleep(2)
    #     # 开始投标
    #     my_setup[1].input_bid(my_params['invest_data'])
    #     if not my_setup[1].invest_button():
    #         assert my_setup[1].bid_button_text() == my_params['value']
    #     else:
    #         my_setup[1].bid_button_click()
    #         assert my_setup[1].invest_fail_info() == my_params['value']
    #         my_setup[1].invest_fail_close()

    @pytest.mark.parametrize('case', BC.fail)
    def test_bid_page_fail(self, my_setup, case):
        my_setup[2].first_ele_click()
        time.sleep(2)
        # 开始投标
        my_setup[1].input_bid(case['invest_data'])
        time.sleep(3)
        assert my_setup[1].bid_button_text() == case['value']

    @pytest.mark.parametrize('wrong_case', BC.wrong_data)
    def test_bid_page_wrong(self, my_setup, wrong_case):
        my_setup[2].first_ele_click()
        time.sleep(2)
        # 开始投标
        my_setup[1].input_bid(wrong_case['invest_data'])
        time.sleep(2)
        my_setup[1].bid_button_click()
        assert my_setup[1].invest_fail_info() == wrong_case['value']
        my_setup[1].invest_fail_close()