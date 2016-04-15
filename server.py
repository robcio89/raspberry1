import socket
import Rpi.GPIO as GPIO
import sys
import os

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind(("192.168.1.111", 12345))
except socket.error:
    print("Failed to bind")
    sys.exit()
mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    print ('Connected by ', addr)
    data = conn.recv(1024)
    if not data:
        break
    if data =="1":
        print ('ONE')
        GPIO.output(7, True)
    if data == "2":
        GPIO.output(7, False)
    conn.sendall(data)
    os.system(str(data))
    conn.sendall(data)

conn.close()
mysock.close()
