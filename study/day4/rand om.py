#! /usr/bin/env python3
# encoding: utf-8
"""
    rand om.py
Created by PythonStudy on 2017/5/20 下午7:28
Copyright 2017 azhen All rights reserved.
"""

import random

# print(random.random())

# print(random.randrange(20))

# print(random.randint(1, 3))

# print(random.choice("azhen"))

# print(random.sample("fsfsfsdf",2))
# a = [1, 2, 3, 4, 5]
# print(random.shuffle(a))
# random.shuffle(a)
checkcode = "1234567890"


a = random.sample(checkcode, 4)

print(a)