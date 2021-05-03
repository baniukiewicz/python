import socket
import threading

local_host = '127.0.0.1'
port = 55666

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind((local_host, port))
        self.sock.listen(True)

    def handler(self, conn, address):
        while True:
            msg = conn.recv(1024)
            for connection in self.connections:
                connection.send(msg)

    def run(self):
        while True:
            conn, address = self.sock.accept()
            thread = threading.Thread(target=self.handler, args=(conn, address))
            thread.start()
            self.connections.append(conn)
            print('coś się połączyło, a dokładniej ', str(address[0]), ':', str(address[1]))

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        while True:
            self.sock.send(bytes(input(''), 'utf-8'))

    def __init__(self):
        self.sock.connect((local_host, port))
        thread = threading.Thread(target=self.send)
        thread.start()
        while True:
            msg = self.sock.recv(1024)
            print(str(msg, 'utf-8'))


if input('server or client? s/c ') == 's':
    serwer = Server()
    serwer.run()
elif 'c':
    client = Client()
