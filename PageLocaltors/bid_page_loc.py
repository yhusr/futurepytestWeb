"""
Time:2020/1/22 0022
"""
from selenium.webdriver.common.by import By


class BidPageLoc:
    # 可用用户余额输入框定位
    user_remainder_loc = (By.XPATH, '//input[@class="form-control invest-unit-investinput"]')
    # 标的余额定位
    bid_Surplus_loc = (By.XPATH, '//span[@class="mo_span4"]')
    # 投标按钮的定位
    bid_confirm_loc = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 激活按钮定位
    active_button_loc =(By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败的提示框信息定位
    invest_fail_info_loc = (By.XPATH, '//div[@class="text-center"]')
    # 投资失败的提示框的关闭
    invest_fail_info_close_loc = (By.XPATH, '//a[text()="确认"]')