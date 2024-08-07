# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:56:14 2024

@author: Camellia
"""
# login_window.py
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)
        self.message_label = QLabel("", self)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)
        self.setLayout(layout)
        
        self.login_button.clicked.connect(self.check_login)
    
    def check_login(self):
        if self.username_input.text() == "user" and self.password_input.text() == "pass":
            self.accept()
        else:
            self.message_label.setText("Invalid username or password")

