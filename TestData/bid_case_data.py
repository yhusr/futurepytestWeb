"""
Time:2020/1/23 0023
"""


class BidCase:
    # 正向用例的数据
    success = {"invest_data": 40000}

    # 反向用例的数据
    fail = [{'invest_data': 123, 'value': '请输入10的整数倍'},
            {'invest_data': 'a', 'value': '请输入10的整数倍'},
            {'invest_data': '8000.55', 'value': '请输入10的整数倍'}]
    wrong_data = [{'invest_data': -80000, 'value': '请正确填写投标金额'},
                  {'invest_data': 50, 'value': '投标金额必须为100的倍数'},
                  {'invest_data': 0, 'value': '请正确填写投标金额'}]
