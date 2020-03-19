"""
Time:2020/1/30 0030
"""
from selenium.webdriver.common.by import By


class HomeWorkPage:
    # 第一个课程的名称
    first_course_name_loc = (By.XPATH, '//div[@class="ktcon2 cl hide"]//strong//a')
    # 作业模块的定位
    homework_in_loc = (By.XPATH, '//div[@id="third-nav"]//a[contains(@href,"homework")]')
    # 上传作业按钮
    homework_upload_loc = (By.XPATH, '//div[@class="announce-cont clearfix"]//a[@class="sc-btn"]')
    # 上传作业选择文件
    file_upload_loc = (By.XPATH, '//div[@class="shangchuan"]//input')
    # 已上传文件的状态
    file_status_loc = (By.XPATH, '//a[@class="succ"]')
    # textarea区域输入内容
    textarea_loc = (By.XPATH, '//textarea[@id="comment"]')
    # textarea区域输入完毕后保存按钮
    textarea_save_button_loc = (By.XPATH, '//div[@class="work-message2 clearfix"]//a')
    # 作业提交成功文本
    homework_submit_text_loc = (By.XPATH, '//div[@class="weui_dialog_bd"]')
    # 作业提交成功关闭提示框按钮
    homework_success_info_close_loc = (By.XPATH, '//a[@class="weui_btn_dialog primary"]')
    # 更新提交的按钮
    update_upload_file_button_loc = (By.XPATH, '//a[@class="new-tj1"]')
    # 确定更新的按钮
    updata_upload_confirm_button_loc = (By.XPATH, '//div[@class="btns"]//a[@class="sure active"]')
    # 点击作业列表中的已提交按钮
    already_submit_button_loc = (By.XPATH, '//a[@class="view-work"]')
    # 点击作业标题进入作业提交界面
    homework_name_loc = (By.XPATH, '//h3[@class="work-title "]//a')
    # 上传文件成功后点击更新提交
    submit_homework_update_loc = (By.XPATH, '//a[@class="new-tj2 active"]')
    # 上传文件成功后点击更新提交后的确定按钮
    submit_homework_update_confirm_loc = (By.XPATH, '//a[@class="weui_btn_dialog primary"]')
    # 保存留言后查看留言的内容
    message_loc = (By.XPATH, '//div[@id="mess1"]//span[@class="s2"]')
