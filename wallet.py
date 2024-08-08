# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:56:13 2024

@author: Camellia
"""

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val