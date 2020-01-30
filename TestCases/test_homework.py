"""
Time:2020/1/30 0030
"""
import pytest
from PageObjects.homework_page import HomeWorkPage
from TestData.homework_case_data import HomeWorkCase


@pytest.mark.mytest
@pytest.mark.usefixtures('home_fre')
class TestHomeWork:
    # 作业文件上传用例
    def test_homework_upload(self, home_fre):
        success_text = HomeWorkPage(home_fre).homework_upload_submit(path=HomeWorkCase.filepath)
        assert HomeWorkCase.success_data['homework_submit'] == success_text

    # 作业留言用例
    def test_homework_message(self, home_fre):
        message_text = HomeWorkPage(home_fre).homework_message(content=HomeWorkCase.success_data['message'])
        assert HomeWorkCase.success_data['message'] == message_text