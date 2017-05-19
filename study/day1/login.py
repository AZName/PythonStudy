#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 17:10:27
# @Author  : xuzhen (azhen@azhen.xin)
# @Link    : http://www.azhen.xin/
# @Version : $Id$

username = input("username:")
password = input("password:")

if "xuzhen" == username:
    if "123" == password:
        print("登录成功")
    else:
        print("账号密码不合法")
else:
    print("账号密码不合法")
