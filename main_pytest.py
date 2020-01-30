"""
Time:2020/1/25 0025
"""
import pytest

if __name__ == '__main__':
    pytest.main(["-m", "mytest", "--reruns",
                 "2", "--reruns-delay", "5",
                 "--junitxml=Outputs/reports/allure.xml"])
