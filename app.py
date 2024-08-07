# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:56:38 2024

@author: Camellia
"""

# app.py
import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from main_window import MainWindow
from PyQt5.QtWidgets import QDialog

def main():
    app = QApplication(sys.argv)
    login = LoginWindow()
    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()
