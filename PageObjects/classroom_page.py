"""
Time:2020/1/12 0012
"""
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from CommonHandle.basepage import BasePage as BP
from PageLocaltors.classroom_page_loc import ClassRoomPage as loc
from TestData.classroom_case_data import ClassRoomCase as RC


class ClassRoomPage:
    def __init__(self, driver:WebDriver(command_executor='http://192.168.31.8:4444/wd/hub')):
        self.driver = driver

    @staticmethod
    def my_account_exist():
        """
        判断登录是否成功，我的账户字样是否显示
        :return: 显示字样返回真，不显示字样返回假
        """
        account_exist_loc = (By.XPATH, '//div[@class="pop-title"]/h3')
        if account_exist_loc:
            return True
        else:
            return False

    # 登录成功后的页面点击关闭弹出的信息提示框
    def info_ele_click(self):
        BP(self.driver).click_ele(loc.info_loc, photo_screen='登录成功后_点击页面信息提示框中的关闭按钮')

    # 点击添加课程按钮后弹出窗口
    def join_course_window(self, attribute):
        # 点击加入课程按钮
        BP(self.driver).click_ele(loc.join_course_button_loc, photo_screen='登录成功后_点击加入课程按钮')
        # 获取添加课程窗口中输入框的属性值
        value = BP(self.driver).get_ele_attribute_value(loc.join_course_input_loc, attribute_name=attribute,
                                                        photo_screen='登录成功后_加入课程窗口_输入窗口的属性值')
        return value

    # 取消添加课程
    def cancle_course(self):
        # 点击加入课程按钮
        BP(self.driver).click_ele(loc.join_course_button_loc, photo_screen='登录成功后_点击加入课程按钮')
        # 取消添加课程
        BP(self.driver).click_ele(loc.join_course_cancle_button_loc, photo_screen='登录成功后_添加课程窗口中点击取消按钮')

    # 添加课程
    def join_course_success(self, join_code):
        # 点击加入课程按钮
        BP(self.driver).click_ele(loc.join_course_button_loc, photo_screen='登录成功后_点击加入课程按钮')
        # 输入课程加课码
        BP(self.driver).input_content(loc.join_course_input_loc, photo_screen='登录成功后_加课码弹出框中输入加课码',
                                      content=join_code)
        # 点击加入课程确定按钮
        time.sleep(2)
        BP(self.driver).wait_ele_able_click(loc.join_course_confirm_button_loc, photo_screen='加课的确定按钮是否可点击')
        BP(self.driver).click_ele(loc.join_course_confirm_button_loc, photo_screen='登录成功后_输入加课码后点击确定')

    # 退课操作
    def drop_course(self, password):
        # 点击查看按钮
        BP(self.driver).click_ele(loc.first_course_more_loc, photo_screen='点击课程中的更多按钮')
        # 点击退课按钮
        BP(self.driver).click_ele(loc.first_course_drop_loc, photo_screen='点击退课按钮退课')
        # 退课框中输入密码
        BP(self.driver).input_content(loc.first_course_drop_input_loc, photo_screen='退课框中输入密码', content=password)
        # 点击退课的确定按钮
        BP(self.driver).click_ele(loc.first_course_drop_confirm_loc, photo_screen='点击退课的确定按钮')

    # 进入班级
    def in_course(self, code):
        # 点击加入课程按钮
        BP(self.driver).click_ele(loc.join_course_button_loc, photo_screen='登录成功后_点击加入课程按钮')
        # 输入课程加课码
        BP(self.driver).input_content(loc.join_course_input_loc, photo_screen='登录成功后_加课码弹出框中输入加课码',
                                      content=code)
        # 点击加入课程确定按钮
        time.sleep(2)
        BP(self.driver).wait_ele_able_click(loc.join_course_confirm_button_loc, photo_screen='加课的确定按钮是否可点击')
        BP(self.driver).click_ele(loc.join_course_confirm_button_loc, photo_screen='登录成功后_输入加课码后点击确定')
        # 点击课程名称进入课堂
        BP(self.driver).click_ele(loc.first_course_name_loc, photo_screen='点击课程名称进入课堂')

    # 判断课程是否添加成功
    def if_course_success(self):
        course_text = BP(self.driver).get_text(loc.join_course_success_text_loc, photo_screen='登录成功后_添加课程成功后的文本')
        if RC.join_course_code['join_code'] in course_text:
            return True
        else:
            return False

    # 判断加课提示是否正确
    def if_course_info(self):
        info_text = BP(self.driver).get_text(loc.join_course_success_info_loc, photo_screen='加课成功的提示文本')
        if info_text == RC.join_course_data['join_success']:
            return True
        else:
            return False

    # 判断退课是否成功
    def drop_courst_info(self):
        drop_info = BP(self.driver).get_text(loc.drop_course_info_loc, photo_screen='退课成功的提示')
        if drop_info == RC.join_course_data['drop_course_info']:
            return True
        else:
            return False

    # 加课码输入错误的提示
    def join_error_course_info(self):
        error_text = BP(self.driver).get_text(loc.join_course_erro_text_loc, photo_screen='输入加课码错误的提示')
        return error_text



