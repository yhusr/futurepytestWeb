"""
Time:2020/1/24 0024
"""
import os
import time

str_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# 当前文件的目录
current_file = os.path.abspath(__file__)
file_path = os.path.dirname(current_file)
root_path = os.path.dirname(file_path)


# outputs目录
output_path = os.path.join(root_path, 'Outputs')
# logs目录
logs_path = os.path.join(output_path, 'logs')
mylog_path = os.path.join(logs_path, 'log{}.log'.format(str_time))
# reports目录
reports_path = os.path.join(output_path, 'reports')
myreport_path = os.path.join(reports_path, 'report{}.html'.format(str_time))
# screenshots目录
screenshots_path = os.path.join(output_path, 'screenshots')