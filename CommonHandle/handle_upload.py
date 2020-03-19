#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xiaojian
# Time: 2019/1/23 20:40

""""""
"""
1、autoIt - .au3 - 
2、SendKeys
3、pywin32

"""
import win32gui
import win32con


# edit - combox - comboBoxEx32 - #32770

# 1\找到输入框和打开按钮 元素；2、输入地址，点击打开。

# 前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。
def upload(filePath, browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""

    # 找元素
    # 一级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", title)
    #
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

    # 往编辑当中，输入文件路径 。
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


# from selenium import webdriver
#
# driver = webdriver.Chrome()
# """
# XXXXXX
# """

# 前一步操作：selenium点击页面的某一个按钮，让上传窗口出现。
# 等待1-2秒。

# 前提：上传窗口要出现！！
# import time
#
# time.sleep(2)
# upload("D:\\chromedriver.log")

# white  - robot whitelibrary
