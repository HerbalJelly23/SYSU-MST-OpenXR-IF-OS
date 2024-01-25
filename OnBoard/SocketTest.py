# 整体流程
# 1. 链接wifi
# 2. 启动网络功能（UDP）
# 3. 接收网络数据
# 4. 处理接收的数据


import socket
import time
import network
import machine


def main():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.scan()


if __name__ == "__main__":
    main()

