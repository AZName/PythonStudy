#! /usr/bin/env python3
# encoding: utf-8
"""
    prople.py
Created by PythonStudy on 2017/5/22 下午2:52
Copyright 2017 azhen All rights reserved.
"""


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s 开始吃啦" % self.name)


class Relation(object):
    def __init__(self):
        print("relation")

    def make_friend(self, obj):

        print(f"{self.name}和{obj.name} 在交朋友", self)


class Man(People, Relation):
    def __init__(self, name, age):
        super(Man, self).__init__(name, age)

m1 = Man("xiaoming", 22)

m2 = Man("xiaohuang", 33)

m2.make_friend(m1)
