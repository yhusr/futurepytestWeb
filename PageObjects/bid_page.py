"""
Time:2020/1/22 0022
"""
from selenium.webdriver.remote.webdriver import WebDriver
from PageLocaltors.bid_page_loc import BidPageLoc as loc
from CommonHandle.basepage import BasePage as BP


class BidPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户可用余额
    def get_user_data(self):
        """
        返回的是string类型的数据
        :return:
        """
        # 等待元素可见
        return BP(self.driver).get_ele_attribute_value(loc.user_remainder_loc, 'data-amount', '投标页面_用户名属性值')

    # 获取标的余额
    def get_bid_surplus(self):
        """
        返回的是string类型的数据
        :return:
        """
        return BP(self.driver).get_text(loc.bid_Surplus_loc, '投标详情页面_可投的余额')

    # 输入投标的金额
    def input_bid(self, data):
        BP(self.driver).input_content(loc.user_remainder_loc, '投标详情页_用户投标金额', data)

    # 点击投标按钮
    def bid_button_click(self):
        BP(self.driver).click_ele(loc.bid_confirm_loc, '投标详情页_点击投标按钮')

    # 获取按钮的文字内容
    def bid_button_text(self):
        return BP(self.driver).get_text(loc.bid_confirm_loc, '投标详情页_确定按钮中的文字')

    # 点击激活按钮
    def active_button_click(self):
        BP(self.driver).click_ele(loc.active_button_loc, '投标成功后弹窗_点击激活按钮')

    # 投资失败的提示信息
    def invest_fail_info(self):
        return BP(self.driver).get_text(loc.invest_fail_info_loc, '投标详情页_投资失败的提示内容')

    # 投资失败的提示信息关闭
    def invest_fail_close(self):
        BP(self.driver).click_ele(loc.invest_fail_info_close_loc, '投标详情页投资失败弹窗_点击弹窗中的关闭按钮')

    # 投资按钮是否正常显示
    def invest_button(self):
        if self.bid_button_text() == '投标':
            return True
        else:
            return False

