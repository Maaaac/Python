#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import numpy as np
#import get_accel
import sys
import smbus
import math
import datetime
import time
from threading import Timer
from signal import signal,SIGPIPE,SIG_DFL
signal(SIGPIPE,SIG_DFL)

host_port = ('192.168.2.60',8080)

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) #or bus = smbus.SMBus(0)
address = 0x68       #This is the address value read the i2cdetect command

bus.write_byte_data(address,power_mgmt_1,0)

class ClientSocket(object):
    def __init__(self):
        # socket.AF_INET用于服务器与服务器之间的网络通信
        # socket.SOCK_STREAM代表基于TCP的流式socket通信
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.client_socket.connect(host_port) #链接服务器
            print("成功连接到服务器")
        except:
            print("连接失败")

    
    def get_time():
        return datetime.datetime.now()

    def read_byte(adr):
        return bus.read_byte_data(address,adr)

    def read_word(adr):
        high = bus.read_byte_data(address,adr)
        low = bus.read_byte_data(address,adr+1)
        val = (high << 8) + low
        return val

#从一个给定的寄存器中读取一个单字（16bits）并将其转化为二进制补码
    def read_word_2c(adr):
        val = read_word(adr)
        if(val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
        
    #得到了每个三维空间中重力对传感器施加的值，通过这个值我们可以计算出X轴和Y轴的旋转值
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def dist_xyz(a,b,c):
        return math.sqrt((a*a)+(b*b)+(c*c))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x,dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y,dist(x,z))
        return math.degrees(radians)    
        
        
        
        
    def run(self):
        def send_data(logfile = None):
            
            gyro_xout = read_word_2c(0x43)
            gyro_yout = read_word_2c(0x45)
            gyro_zout = read_word_2c(0x47)

            gyro_x=gyro_xout / 131
            gyro_y=gyro_yout / 131
            gyro_z=gyro_zout / 131

#读取XYZ的加速度计数值，MPU6050传感器有许多寄存器，他们具有不同的功能，用于加速数据的寄存器是0x3b、0x3d、0x3f
            accel_xout = read_word_2c(0x3b)
            accel_yout = read_word_2c(0x3d)
            accel_zout = read_word_2c(0x3f)
            
            #需要应用到原始加速度计值的默认转换值是16384
            accel_xout_scaled = accel_xout / 16384.0
            accel_yout_scaled = accel_yout / 16384.0
            accel_zout_scaled = accel_zout / 16384.0
            accel_xyz = dist_xyz(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)
           # data=get_accel.accel_xyz
           #data="tuoluoyishuju"+"\r\n"
           #send=str(data)
         
            #self.client_socket.sendall(send.encode('utf-8'))
            send=str(gyro_x)+str(gyro_y)+str(gyro_z)+str(accel_xyz)
            self.client_socket.sendall(send.encode())
            if logfile:
                logfile.write(line)
            Timer(0.2,send_data).start()
        send_data()
        #self.clint_socket.close()
        
        
if __name__ == '__main__':
    s = ClientSocket()
    s.run()
