#! /usr/bin/env python3
# encoding: utf-8
"""
    dog.py
Created by PythonStudy on 2017/5/21 下午7:32
Copyright 2017 azhen All rights reserved.
"""


class Dog:
    def egt(self):
        print(self, "汪汪汪汪汪汪汪汪")


d1 = Dog()

d1.egt()


class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47')  # 生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
r1.buy_gun("ak47")
