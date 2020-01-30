"""
Time:2020/1/30 0030
"""
from selenium.webdriver.common.by import By
from TestData.private_letter_case_data import PrivateLetterData as PD


class PrivateLetter:
    into_private_letter_loc = (By.XPATH, '//div[@class="privateLetter"]//a')
    private_letter_textarea_loc = (By.XPATH, '//textarea[@class="ps-container"]')
    sent_letter_button_loc = (By.XPATH, '//a[@class="btn btn-positive"]')
    sent_letter_text_loc = (By.XPATH, '//div[text()="'+PD.success_data['letter_message']+'"]')
