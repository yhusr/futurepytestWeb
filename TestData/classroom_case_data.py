"""
Time:2020/1/23 0023
"""


class ClassRoomCase:
    # 正向用例的数据
    join_course_code = {'join_code': 'P69UVV'}
    # 点击加入课程后的显示数据
    join_course_data = {"join_attribute": 'placeholder', "join_info": '请输入课程加课验证码',
                        "join_success": '加入课堂成功', "drop_course_info": '课程退课成功'}

    # 反向用例的数据
    join_course_error = [{'course_code': 'P69UVV1', 'value': '该加课码不存在或者已经失效'},
                         {'course_code': 'P69UV', 'value': '加课验证码必须是6位字符'}]

