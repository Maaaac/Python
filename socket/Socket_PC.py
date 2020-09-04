#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import numpy
import datetime
address = ('192.168.2.60',8080) # 设置地址与端口，如果是接收任意ip对本服务器的连接，地址栏可空，但端口必须设置

class ServerSocket(object):
    def __init__(self):
        # socket.AF_INET用于服务器与服务器之间的网络通信
        # socket.SOCK_STREAM代表基于TCP的流式socket通信
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(address) # 将Socket（套接字）绑定到地址
        self.server_socket.listen(True) # 开始监听TCP传入连接
        print("Waiting for messages...")
 
    def run(self):
# 接受TCP链接并返回（conn, addr），其中conn是新的套接字对象，可以用来接收和发送数据，addr是链接客户端的地址。
        conn, addr = self.server_socket.accept()
        while True:
            print("连接成功")
            msg_data=conn.recv(1024)
            msg_data=msg_data.decode()
            print(msg_data,datetime.datetime.now(),'\n')

       # self.server_socket.close()

if __name__ == '__main__':
    s = ServerSocket()
    s.run()
