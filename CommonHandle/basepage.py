"""
Time:2020/1/23 0023
"""
import datetime
import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from CommonHandle.handle_os import logs_path,screenshots_path,reports_path
from CommonHandle.handle_log import logger


class BasePage:

    def __init__(self, driver:WebDriver(command_executor='http://192.168.31.8:4444/wd/hub')):
        self.driver = driver

    # 等待元素可见
    def ele_wait(self, loc, photo_screen, timeout=30, frequency=0.5):
        start_time = datetime.datetime.now()
        try:
            ww(self.driver, timeout, poll_frequency=frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger.exception(f'等待{photo_screen}_{loc}元素失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'等待{photo_screen}_{loc}元素可见成功。')
            end_time = datetime.datetime.now()
            logger.info('起始时间：{}，开始时间：{}，总计时长：{}'.format(start_time, end_time, end_time-start_time))

    # 等待元素可点击
    def wait_ele_able_click(self, loc, photo_screen, timeout=30, frequency=0.5):
        start_time = datetime.datetime.now()
        try:
            ww(self.driver, timeout, poll_frequency=frequency).until(EC.element_to_be_clickable(loc))
        except:
            logger.exception(f'等待{photo_screen}_{loc}元素可点击失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'等待{photo_screen}_{loc}元素可点击成功。')
            end_time = datetime.datetime.now()
            logger.info('起始时间：{}，开始时间：{}，总计时长：{}'.format(start_time, end_time, end_time - start_time))

    # 查找元素的封装
    def find_ele(self, loc, photo_screen):
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception(f'查找{photo_screen}_{loc}元素失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'查找{photo_screen}_{loc}元素成功。')
            return ele

    # 点击元素的封装
    def click_ele(self, loc, photo_screen, timeout=30, frequency=0.5):
        self.ele_wait(loc, photo_screen, timeout, frequency)
        self.wait_ele_able_click(loc, photo_screen, timeout, frequency)
        ele = self.find_ele(loc, photo_screen)
        try:
            ele.click()
        except:
            logger.exception(f'点击{photo_screen}_{loc}元素失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'{photo_screen}_{loc}元素点击成功。')

    # 输入内容
    def input_content(self, loc, photo_screen, content, timeout=30, frequency=0.5):
        self.ele_wait(loc, photo_screen, timeout, frequency)
        ele = self.find_ele(loc, photo_screen)
        try:
            ele.send_keys(content)
        except:
            logger.exception(f'在{photo_screen}_{loc}元素输入内容失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'{photo_screen}_{loc}元素中输入内容成功。')

    # 获取文本
    def get_text(self, loc, photo_screen, timeout=30):
        self.ele_wait(loc, photo_screen, timeout)
        ele = self.find_ele(loc, photo_screen)
        try:
            ele_text = ele.text
        except:
            logger.exception(f'在{photo_screen}_{loc}元素中获取文本内容失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'{photo_screen}_{loc}元素中获取文本内容_{ele_text}_成功。')
            return ele_text

    # 获取属性值
    def get_ele_attribute_value(self, loc, attribute_name, photo_screen, timeout=30, frequency=0.5):
        self.ele_wait(loc, photo_screen, timeout, frequency)
        ele = self.find_ele(loc, photo_screen)
        try:
            ele_text = ele.get_attribute(attribute_name)
        except:
            logger.exception(f'在{photo_screen}_{loc}元素中获取属性值失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info(f'{photo_screen}_{loc}元素中获取属性值成功。')
            return ele_text

    # 获取所有window句柄
    def get_window_handles(self, photo_screen):
        try:
            all_handles = self.driver.window_handles
        except:
            logger.exception(f'在{photo_screen}页面中获取当前所有句柄失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.exception(f'在{photo_screen}页面中获取当前所有句柄成功')
            return all_handles

    # 获取最新window句柄
    def switch_handle(self, photo_screen):
        try:
            new_handle = self.get_window_handles(photo_screen)[-1]
            self.driver.switch_to.window(new_handle)
        except:
            logger.exception(f'在{photo_screen}页面中切换到最新handle失败')
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.exception(f'在{photo_screen}页面中切换到最新的handle成功')

    # 截图的保存封装
    def _sreen_shots_filename(self, photo_screen):
        # filename 图片的名称
        filename = '{}_{}.png'.format(photo_screen, time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))

        # 截图存放的路径
        file_path = os.path.join(screenshots_path, filename)
        try:
            self.driver.save_screenshot(file_path)
        except:
            logger.exception('图片{}存放失败'.format(filename))
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info('图片{}存放成功'.format(filename))

    # 滚动到指定元素可见
    def visible_ele_roll(self, loc, photo_screen):
        ele = self.find_ele(loc, photo_screen=photo_screen)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
        except:
            logger.exception('滚动到元素{}失败'.format(loc))
            # photoscreen命名格式：页面名称_行为名称_年时分秒.png
            self._sreen_shots_filename(photo_screen)
            raise
        else:
            logger.info('滚动到元素{}成功'.format(loc))


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    loc = (By.ID, 'kw')
    BasePage(driver).ele_wait(loc, photo_screen='百度首页_搜索栏')
    BasePage(driver).input_content(loc, photo_screen='百度首页_搜索栏', content='柠檬班')
    ele = BasePage(driver).find_ele(loc, photo_screen='百度首页_搜索栏')
    driver.quit()
