import random
from machine import Pin, SPI
from PyDrive import  st7789
from PyDrive import  st7789py
from romfonts import vga2_bold_16x32 as font


# 解决第1次启动时，不亮的问题
st7789.ST7789(SPI(2, 60000000), dc=Pin(2), cs=Pin(5), rst=Pin(15))

# 创建显示屏对象
tft = st7789py.ST7789(SPI(2, 60000000), 240, 240, reset=Pin(15), dc=Pin(2), cs=Pin(5), rotation=0)

# 屏幕显示蓝色
tft.fill(0)

# 显示Hello
# tft.text(font, "Hello", 0, 0, st7789py.color565(255, 0, 0), st7789py.color565(0, 0, 255))

def show_text():
    for rotation in range(4):
        tft.rotation(rotation)
        tft.fill(0)
        col_max = tft.width - font.WIDTH*6
        row_max = tft.height - font.HEIGHT

        for _ in range(100):
            tft.text(
                font,
                "Hello!",
                random.randint(0, col_max),
                random.randint(0, row_max),
                st7789py.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)),
                st7789py.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
            )

# 随机显示Hello!
while True:
   show_text()
