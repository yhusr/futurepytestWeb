"""
Time:2020/1/22 0022
"""
from selenium.webdriver.common.by import By


class ClassRoomPage:
    # 关闭提示框按钮
    info_loc = (By.XPATH, '//a[@class="close"]')
    # 加入课程按钮
    join_course_button_loc = (By.XPATH, '//div[@class="ktcon1l fr"]')
    # 输入课程加课验证码
    join_course_input_loc = (By.XPATH, '//div[@class="chuangjiankccon"]/input')
    # 加入课程的取消按钮
    join_course_cancle_button_loc = (By.XPATH, '//a[@class="btn btn-defalut"]')
    # 加入课程的确定按钮
    join_course_confirm_button_loc = (By.XPATH, '//a[text()="加入"]')
    # 加入课程成功后的文字显示
    join_course_success_text_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//p[@class="invitecode"]')
    # 加入课程成功后的文字提示
    join_course_success_info_loc = (By.XPATH, '//div[@id="show-tip"]//span')
    # 第一个课程的名称
    first_course_name_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//strong//a')
    # 第一个课程的更多按钮
    first_course_more_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//a[@class="kdmore"]')
    # 第一个课程更多下的退课按钮
    first_course_drop_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//li[@class="kdli3"]/a')
    # 第一个课程退课输入密码框
    first_course_drop_input_loc = (By.XPATH, '//input[@type="password"]')
    # 第一个课程退课的确定按钮
    first_course_drop_confirm_loc = (By.XPATH, '//div[@class="deletebot cl"]//a[text()="退课"]')
    # 退课成功的提示
    drop_course_info_loc = (By.XPATH, '//div[@id="show-tip"]//span')
    # 第一个课程退课的取消按钮
    first_course_drop_cancle_loc = (By.XPATH, '//div[@class="guidang"]//a[@class="btn btn-default"]')
    # 第一个课程更多下的归档按钮
    first_course_file_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//li[@class="kdli2"]/a')
    # 第一个课程归档的取消按钮
    first_course_file_cancle_loc = (By.XPATH, '//div[@class="guidang"]//a[@class="btn btn-default"]')
    # 第一个课程归档的确定按钮
    first_course_file_confirm_loc = (By.XPATH, '//div[@class="guidang"]//a[@class="btn btn-positive"]')
    # 归档成功的提示文本
    file_success_loc = (By.XPATH, '//div[@id="show-tip"]//span')
    # 归档管理按钮
    file_manage_loc = (By.XPATH, '//li[@class="ktli2"]//a')
    # 私信按钮
    private_letter_loc = (By.XPATH, '//div[@class="privateLetter"]//a')

    # 加课输入错误时的提示
    join_course_erro_text_loc = (By.XPATH, '//div[@id="error-tip"]//span')

    # 进入班级的文本定位
    classroom_text_loc = (By.XPATH, '//div[@id="third-nav"]//a[@class="active"]')
