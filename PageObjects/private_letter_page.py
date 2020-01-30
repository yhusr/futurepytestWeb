"""
Time:2020/1/30 0030
"""
import time
from selenium.webdriver.remote.webdriver import WebDriver
from CommonHandle.basepage import BasePage as BP
from PageLocaltors.private_letter_page_loc import PrivateLetter as loc


class PrivateLetter:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 点击私信按钮进入私信页面输入并发送
    def go_into_private_letter(self, content):
        BP(self.driver).click_ele(loc.into_private_letter_loc, photo_screen='点击私信进入私信页面')
        time.sleep(2)
        BP(self.driver).get_window_handles(photo_screen='查看所有的handles')
        BP(self.driver).switch_handle(photo_screen='切换handle至私信界面')
        BP(self.driver).click_ele(loc.private_letter_textarea_loc, photo_screen='点击输入框')
        BP(self.driver).input_content(loc.private_letter_textarea_loc, photo_screen='输入框中输入内容', content=content)
        BP(self.driver).wait_ele_able_click(loc.sent_letter_button_loc, photo_screen='等待发送按钮变为可点击状态')
        BP(self.driver).click_ele(loc.sent_letter_button_loc, photo_screen='点击发送按钮发送输入的私信内容')

    # 判断内容是否发送成功
    def if_sent_text(self, sent_message):
        try:
            BP(self.driver).find_ele(loc.sent_letter_text_loc, photo_screen='发送成功后的文本定位')
        except Exception as e:
            return False
        else:
            return True
