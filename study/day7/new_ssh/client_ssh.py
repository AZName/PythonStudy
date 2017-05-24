#! /usr/bin/env python3
# encoding: utf-8
"""
    client_ssh.py
Created by PythonStudy on 2017/5/24 下午5:49
Copyright 2017 azhen All rights reserved.
"""

import socket


client = socket.socket()

client.connect(("localhost", 20000))


while True:

    cmd = input(">>:")
    if not len(cmd): continue

    client.send(cmd.encode("utf-8"))

    data_size = client.recv(1024).decode()
    client.send(b"1")
    data = b""

    data_size = int(data_size)

    print(data_size)

    while data_size > 0:

        tmp = client.recv(1024)

        data_size -= len(tmp)

        data += tmp

    else:
        print(f"输出{data.decode()}")

client.close()