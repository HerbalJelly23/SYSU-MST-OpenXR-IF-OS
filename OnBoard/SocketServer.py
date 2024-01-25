#ESP32运行相关代码
import network
import socket
import time
import machine

SSID="TP-LINK-Swift"
# SSID="192.168.0.106"
PASSWORD="yzy2003123yzy"
port=8080
wlan=None
listenSocket=None
led2 = machine.Pin(2, machine.Pin.OUT)
wlan=network.WLAN(network.STA_IF)         #create a wlan object
    

def connectWifi(ssid,passwd):
    wlan.active(True)                         #Activate the network interface
    wlan.disconnect()                         #Disconnect the last connected WiFi
    if not wlan.isconnected():
        print('Connecting to Network...')
        wlan.connect(ssid,passwd)                 #connect wifi
        i = 1
        while not wlan.isconnected():
            print(f"Connecting...[{i}]")
            i += 1
            time.sleep_ms(500)
    print('Network Config:', wlan.ifconfig())
    return True


def main():
    # Catch exceptions,stop program if interrupted accidentally in the 'try'
    try:
        connectWifi(SSID,PASSWORD)
        ip=wlan.ifconfig()[0]                     #get ip addr
        listenSocket = socket.socket()            #create socket
        listenSocket.bind((ip,port))              #bind ip and port
        listenSocket.listen(1)                    #listen message
        listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #Set the value of the given socket option
        print ('TCP Waiting...')

        while True:
            print("Accepting.....")
            conn,addr = listenSocket.accept()       #Accept a connection,conn is a new socket object
            print(addr,"Connected")
            while True:
                print('Ready to Receive...')
                recv_data = conn.recv(1024)
                if(len(recv_data) == 0):
                    print("Close Socket")
                    conn.close()                        #if there is no data,close
                    break
                print(f"{addr} Send: {recv_data}")
                recv_data_str = recv_data.decode("utf-8")
                try:
                    print(recv_data_str)
                    if recv_data_str == "ON" or recv_data_str == "on":
                        print("这里是要灯亮的代码...")
                        led2.value(1)
                    elif recv_data_str == "OFF" or recv_data_str == "off":
                        print("这里是要灯灭的代码...")
                        led2.value(0)
                except Exception as ret:
                    print("error:", ret)
                
                
    except:
        if(listenSocket):
            listenSocket.close()
        wlan.disconnect()
        wlan.active(False)

if __name__ == "__main__":
    main()
