#! /usr/bin/env python3
# encoding: utf-8
"""
    Calculator.py
Created by PythonStudy on 2017/5/21 下午4:34
Copyright 2017 azhen All rights reserved.
"""
# 计算器
import re

# formula = input("请输入：")
formula = "1-3+3*4/5*(123+123/(1231*2))"

# a = re.findall("[0-9]{1,1000000000}", formula)
# a = re.findall(r"[[0-9]{1,1000000000}[-+*/]()]{1}", formula)
a = re.split(r"\W", formula)
print(a)


c = 1-3+3*4/5*(123+123/(1231*2))
print(c)