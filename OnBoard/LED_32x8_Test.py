import time
from PyDrive import max7219
from machine import Pin, SoftSPI, RTC


class Clock:
    """
    定义可以用来控制32x8的点阵屏类
    """
    def __init__(self):
        self.dp()
        self.se = 0
        self.rtc=RTC()

    def dp(self):
        spi = SoftSPI(baudrate=100000, polarity=1, phase=0, mosi=Pin(27),sck=Pin(25), miso=Pin(32))  # miso没用到，随便设置一个GPIO即可
        self.display = max7219.Matrix8x8(spi,Pin(26),4)

    def show_time(self):
        
        date = self.rtc.datetime()
        self.m = date[5]
        self.h = date[4]
        self.display.fill(1)
        self.display.text(str(self.h) if len(str(self.h))==2 else ' ' + str(self.h) , 0, 1, 0)
        self.display.pixel(16, 3, self.se)        
        self.display.pixel(16, 5, self.se)
        self.display.pixel(15, 3, self.se)        
        self.display.pixel(15, 5, self.se)    
        self.display.text(str(self.m) if len(str(self.m))==2 else '0' + str(self.m) , 16, 1, 0)
        self.se = 0 if self.se == 1 else 1
        """
        self.display.text('abAB45678', 0, 0, 1)
        """
        self.display.show()
        


# 1. 创建对象
clock = Clock()

# 2. 调用显示
while True:
    clock.show_time()
    time.sleep_ms(1000)

