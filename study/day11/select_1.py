#! /usr/bin/env python3
# encoding: utf-8
"""
    select_1.py
Created by PythonStudy on 2017/5/31 下午3:42
Copyright 2017 azhen All rights reserved.
"""
import select, socket


server = socket.socket()

server.bind(("localhost", 9000))
server.listen()

select.select()