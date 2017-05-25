#! /usr/bin/env python3
# encoding: utf-8
"""
    ftp_server.py
Created by PythonStudy on 2017/5/25 上午9:54
Copyright 2017 azhen All rights reserved.
"""

import socket, os, hashlib

ftp_server = socket.socket()

ftp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 重复利用一个端口

ftp_server.bind(("localhost", 1993))

ftp_server.listen()

while True:
    conn, arrt = ftp_server.accept()
    print("开始接受数据", arrt)

    while True:
        data = conn.recv(1024)

        if not data:
            print("客户端不存在")
            break
        file_name = data.decode().split()
        if os.path.isfile(file_name):
            m = hashlib.md5() # 文件验证

            with open(file=file_name, mode="rb") as f:
                for line in f:
                    m.update(line)
                    conn.send(line)

            print(m.hexdigest())


ftp_server.close()





