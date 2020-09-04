import smbus
import math
import datetime

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

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

bus = smbus.SMBus(1) #or bus = smbus.SMBus(0)
address = 0x68       #This is the address value read the i2cdetect command

bus.write_byte_data(address,power_mgmt_1,0)
counter = 1
while(counter>0):
    print("-----------------",counter,"-----------------")
    print("-------------",get_time(),"------------")
    print("-------------陀螺仪数据-------------")

    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

#除以131，可以得到每秒的旋转度数
    print("X轴陀螺仪计原始数值：",gyro_xout,"每秒的旋转度数:",(gyro_xout / 131))
    print("Y轴陀螺仪计原始数值：",gyro_yout,"每秒的旋转度数:",(gyro_yout / 131))
    print("Z轴陀螺仪计原始数值：",gyro_zout,"每秒的旋转度数:",(gyro_zout / 131),"\n")

    print("-------------加速度数据-------------")

#读取XYZ的加速度计数值，MPU6050传感器有许多寄存器，他们具有不同的功能，用于加速数据的寄存器是0x3b、0x3d、0x3f
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

#需要应用到原始加速度计值的默认转换值是16384
    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print("X轴加速度计原始数值:",accel_xout,"真实加速度",accel_xout_scaled)
    print("Y轴加速度计原始数值:",accel_yout,"真实加速度",accel_yout_scaled)
    print("Z轴加速度计原始数值:",accel_zout,"真实加速度",accel_zout_scaled)

    print("----------------------------------")
#计算出了X轴和Y轴的旋转角度
    print("X轴旋转度数:",get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    print("X轴旋转度数:",get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    print("三轴和加速度:",dist_xyz(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    counter =counter +  1