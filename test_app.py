# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:56:57 2024

@author: Camellia
"""

# test_app.py
import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from login_window import LoginWindow
from main_window import MainWindow

def test_login_success(qtbot):
    login = LoginWindow()
    qtbot.addWidget(login)
    
    # 输入正确的用户名和密码
    qtbot.keyClicks(login.username_input, "user")
    qtbot.keyClicks(login.password_input, "pass")
    
    # 模拟点击登录按钮
    qtbot.mouseClick(login.login_button, Qt.LeftButton)
    
    # 验证登录成功
    assert login.result() == QDialog.Accepted

def test_login_failure(qtbot):
    login = LoginWindow()
    qtbot.addWidget(login)
    
    # 输入错误的用户名和密码
    qtbot.keyClicks(login.username_input, "wrong_user")
    qtbot.keyClicks(login.password_input, "wrong_pass")
    
    # 模拟点击登录按钮
    qtbot.mouseClick(login.login_button, Qt.LeftButton)
    
    # 验证登录失败
    assert login.message_label.text() == "Invalid username or password"

def test_main_window(qtbot):
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    
    # 验证主窗口显示正确的欢迎消息
    assert main_window.label.text() == "Welcome to the main window!!!!!"

def call():
    pass

# #########test
# !pytest

