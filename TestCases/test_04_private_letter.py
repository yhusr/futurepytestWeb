"""
Time:2020/1/30 0030
"""
import time
import pytest
from TestData.private_letter_case_data import PrivateLetterData as PD
from PageObjects.private_letter_page import PrivateLetter as PL


@pytest.mark.master
@pytest.mark.mytest
@pytest.mark.usefixtures('letter')
class TestPrivateLetter:
    # 进入私信并发送内容
    def test_sent_private(self, home_fre):
        PL(home_fre).go_into_private_letter(content=PD.success_data['letter_message'])
        assert PL(home_fre).if_sent_text(sent_message=PD.success_data['letter_message'])
