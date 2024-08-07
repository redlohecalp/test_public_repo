# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:56:12 2024.

@author: Camellia
"""
# main_window.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.label = QLabel("Welcome to the main window!", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
