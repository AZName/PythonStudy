#! /usr/bin/env python3
# encoding: utf-8
"""
    hash_lib.py
Created by PythonStudy on 2017/5/21 下午2:23
Copyright 2017 azhen All rights reserved.
"""

# 加密模块

import hashlib
import hmac

M = hashlib.md5()

M.update("徐振".encode(encoding="utf-8"))

print(M.hexdigest())

h = hmac.new("天王盖地虎".encode(encoding="utf-8"), "小鸡蘑菇".encode(encoding="utf-8"))
print(h.hexdigest())