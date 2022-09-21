from socket import *
from time import sleep

if __name__ == '__main__':
    dest = ("172.168.35.255", 6666)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    data = "I am not Qt"
    while True:
        sleep(2)
        s.sendto(data.encode(), dest)
    s.close()
