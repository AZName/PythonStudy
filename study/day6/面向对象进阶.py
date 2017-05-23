#! /usr/bin/env python3
# encoding: utf-8
"""
    面向对象进阶.py
Created by PythonStudy on 2017/5/23 上午10:15
Copyright 2017 azhen All rights reserved.
"""


class Dog(object):
    def __init__(self, name):
        self.name = name
    # @classmethod
    # @staticmethod
    @property
    def eat(self, food):
        print(f"{self.name}开始吃{food}")


d = Dog("小狗")
d.eat("包子")