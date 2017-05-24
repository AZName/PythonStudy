#! /usr/bin/env python3
# encoding: utf-8
"""
    server.py
Created by PythonStudy on 2017/5/24 下午1:12
Copyright 2017 azhen All rights reserved.
"""

import socket

server = socket.socket()

server.bind(("localhost", 5656))

server.listen()

conn, addr = server.accept()

data = conn.recv(1024)
print(data.decode())

conn.send(data.upper())

server.close()