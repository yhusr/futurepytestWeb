"""
Time:2020/1/30 0030
"""
import time
from selenium.webdriver.remote.webdriver import WebDriver
from CommonHandle.basepage import BasePage as BP
from PageLocaltors.homework_page_loc import HomeWorkPage as loc
from PageObjects.classroom_page import ClassRoomPage as CR
from TestData.classroom_case_data import ClassRoomCase as data


class HomeWorkPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 进入作业提交模块
    def homework_submit_page(self):
        CR(self.driver).join_course_success(data.join_course_code['join_code'])
        time.sleep(2)
        BP(self.driver).click_ele(loc.first_course_name_loc, photo_screen='点击作业名称，进入作业界面')
        # 点击进入作业模块
        BP(self.driver).click_ele(loc.homework_in_loc, photo_screen='点击作业模块，进入作业模块界面')
        # 点击作业标题进入作业提交
        BP(self.driver).click_ele(loc.homework_name_loc, photo_screen='点击作业名称进入作业提交界面')
        BP(self.driver).click_ele(loc.update_upload_file_button_loc, photo_screen='点击更新提交按钮')
        time.sleep(2)
        BP(self.driver).click_ele(loc.updata_upload_confirm_button_loc, photo_screen='确定更新按钮')

    # 上传作业
    def homework_upload_submit(self, path):
        self.homework_submit_page()
        time.sleep(2)
        BP(self.driver).input_content(loc.file_upload_loc, photo_screen='点击上传文件按钮', content=path)
        BP(self.driver).click_ele(loc.submit_homework_update_loc, photo_screen='上传作业后更新提交')
        time.sleep(2)
        success_text = BP(self.driver).get_text(loc.homework_submit_text_loc, photo_screen='获取更新成功后的提示文本')
        BP(self.driver).click_ele(loc.submit_homework_update_confirm_loc, photo_screen='更新提交后确定')
        return success_text

    # 作业留言
    def homework_message(self, content):
        self.homework_submit_page()
        time.sleep(2)
        BP(self.driver).visible_ele_roll(loc.message_loc, photo_screen='滑动页面至元素位置')
        BP(self.driver).click_ele(loc.message_loc, photo_screen='点击留言回复处')
        self.driver.execute_script("var a = document.getElementById('comment');a.innerText = '"+content+" '")
        BP(self.driver).click_ele(loc.textarea_save_button_loc, photo_screen='保存作业留言')
        message_text = BP(self.driver).get_text(loc.message_loc, photo_screen='获取作业留言的内容')
        BP(self.driver).click_ele(loc.submit_homework_update_loc, photo_screen='上传作业后更新提交')
        time.sleep(2)
        BP(self.driver).click_ele(loc.submit_homework_update_confirm_loc, photo_screen='更新提交后确定')
        return message_text



