"""
Time:2020/1/15 0015
"""


class LoginData:
    # 正向登录用例的数据
    right_data = {'username': '18684720553', 'password': 'python'}

    # 反向登录用例的数据
    error_data = [{'username': '', 'password': 'python', 'value': '请输入手机号'},
                  {'username': '18684720553', 'password': '', 'value': '请输入密码'},
                  {'username': '', 'password': '', 'value': '请输入手机号'}]