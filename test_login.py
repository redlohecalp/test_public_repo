# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:41:08 2024

@author: Camellia
"""

import unittest
# import coverage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from login import LoginWindow

class TestLoginWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.login_window = LoginWindow()
        self.login_window.show()

    def tearDown(self):
        self.login_window.close()

    def test_login_success(self):
        QTest.keyClicks(self.login_window.username_input, 'admin')
        QTest.keyClicks(self.login_window.password_input, 'password')
        QTest.mouseClick(self.login_window.login_button, Qt.LeftButton)

        self.assertEqual(self.login_window.username_input.text(), 'admin')
        self.assertEqual(self.login_window.password_input.text(), 'password')

    def test_login_failure(self):
        QTest.keyClicks(self.login_window.username_input, 'user')
        QTest.keyClicks(self.login_window.password_input, 'wrongpassword')
        QTest.mouseClick(self.login_window.login_button, Qt.LeftButton)

        self.assertEqual(self.login_window.username_input.text(), 'user')
        self.assertEqual(self.login_window.password_input.text(), 'wrongpassword')

if __name__ == '__main__':
    # cov = coverage.Coverage()
    # cov.start()
    
    # loader = unittest.TestLoader()
    # tests = loader.discover('.')
    # testRunner = unittest.runner.TextTestRunner()
    # testRunner.run(tests)
    
    # cov.stop()
    # # cov.save()
    # cov.report(show_missing=True)
    # # cov.html_report(directory='htmlcov')
    unittest.main()
