#! /usr/bin/env python3
# encoding: utf-8
"""
    121_socket.py
Created by PythonStudy on 2017/5/24 上午11:50
Copyright 2017 azhen All rights reserved.
"""

import socket

client = socket.socket()


client.connect(("localhost", 9999))

while True:
    msg = input(">>:")
    client.send(msg.encode())

    print(client.recv(1024).decode())

client.close()

