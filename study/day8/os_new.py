#! /usr/bin/env python3
# encoding: utf-8
"""
    os_new.py
Created by PythonStudy on 2017/5/25 下午4:00
Copyright 2017 azhen All rights reserved.
"""

import os


print(os.getcwd())

while True:
    msg = input(">>:").rstrip()
    print(msg.strip())
    if ".." in msg:
        print(os.getcwd())
        os.chdir(os.pardir())
        print(os.getcwd())
    # else:
    #
    #     data = os.popen(msg).read()
    #     print(data)

