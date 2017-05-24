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

    def __str__(self):
        return "xuzhen"

d1 = Dog()

# d1.egt()

d1.__str__()


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


def show():
    print("天天不开心")
    pass


class Porple_row(object):
    age = 200  #类变量 公用属性（数据）节省开销

    def __del__(self):
        print("已经释放内存")

    def __init__(self):
        self.name = "徐振"
        self.__type = "就是不告诉你"

    def test(self):
        for a in range(18):
            print(a, self)
            self.__type = "我的天"
            print(self.__type)
        pass


por = Porple_row()

por2 = Porple_row()

# por.age = 190


print(Porple_row.age)
Porple_row.age = 190
print(por)
por.test()

del por


