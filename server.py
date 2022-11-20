import socket
from _thread import *

cilent_socket = []

def threaded(cilent_socket, addr):
    print("Connected by:" + addr[0], ':',  addr[1])
    
    while True:
        try:
            data = client_socket.recv(1024)

