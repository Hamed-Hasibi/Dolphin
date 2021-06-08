# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import binascii

import Config_pb2
import Messages_pb2

from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        # hexvalue = binascii.hexlify(data).decode("utf-8")
        # print(hexvalue)
        # print(type(hexvalue))

        #print(type(hexvalue))
        #if(hexvalue[0:3] == 'abab'):
            #print(hexvalue)


        # buf = data
        # n = 0
        # while n < len(buf):
        #     msg_len, new_pos = _DecodeVarint32(buf, n)
        #     n = new_pos
        #     msg_buf = buf[n:n + msg_len]
        #     n += msg_len
        #     read_metric = Messages_pb2.DataPoint
        #     read_metric.ParseFromString(msg_buf)
        #     # do something with read_metric

        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        # data = data[::-1]

        # send back reversed string to client
        # c.send(data)

    # connection closed
    c.close()


def Main():
    host = "0.0.0.0"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 8086
    # s = socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
