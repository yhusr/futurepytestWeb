"""
Time:2020/1/22 0022
"""
import time
import pytest
from TestData.classroom_case_data import ClassRoomCase as RC
from TestData.common_data import WebCommon


@pytest.mark.master
@pytest.mark.usefixtures('my_setup')
class TestClassRoom:
    # 正向投标用例
    # 加入课程弹窗是否成功
    def test_join_course_window(self, my_setup):
        my_setup[1].info_ele_click()
        time.sleep(2)
        # 加入课程弹窗并获取输入框的属性值
        input_value = my_setup[1].join_course_window(attribute=RC.join_course_data['join_attribute'])
        assert input_value == RC.join_course_data['join_info']

    # 加入课程是否成功
    def test_join_course(self, my_setup):
        my_setup[1].info_ele_click()
        time.sleep(2)
        # 加入课程
        my_setup[1].join_course_success(join_code=RC.join_course_code['join_code'])
        assert my_setup[1].if_course_info()
        assert my_setup[1].if_course_success()

    # 取消加入课程
    def test_cancle_join_course(self, my_setup):
        my_setup[1].info_ele_click()
        time.sleep(2)
        my_setup[1].cancle_course()

    # 退课
    def test_drop_course(self, my_setup):
        my_setup[1].info_ele_click()
        time.sleep(2)
        my_setup[1].drop_course(WebCommon.password)
        assert my_setup[1].drop_courst_info()

    # 进入课堂页面
    def test_class_page(self, my_setup):
        my_setup[1].info_ele_click()
        time.sleep(2)
        my_setup[1].in_course(code=RC.join_course_code['join_code'])
        time.sleep(2)
        current_url = my_setup[0].current_url
        assert WebCommon.index_url != current_url
        my_setup[0].back()
        my_setup[1].drop_course(WebCommon.password)

    # 反向加课用例
    @pytest.mark.parametrize('my_params', RC.join_course_error)
    def test_classroom_page_fail(self, my_setup, my_params):
        my_setup[1].info_ele_click()
        time.sleep(2)
        # 加入课程
        my_setup[1].join_course_success(join_code=my_params['course_code'])
        error_text = my_setup[1].join_error_course_info()
        assert error_text == my_params['value']