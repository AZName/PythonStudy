#! /usr/bin/env python3
# encoding: utf-8
"""
    guess.py
Created by PythonStudy on 2017/5/19 下午1:26
Copyright 2017 azhen All rights reserved.
"""
age_of_boy = 56

while True:
    gueed_age = int(input("gueed age:"))

    if gueed_age > age_of_boy:
        print("猜大了")
    elif gueed_age < age_of_boy:
        print("猜小了")
    else:
        print("恭喜你才对了!")
        break
