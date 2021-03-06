#!/usr/bin/env python2
import json
import socket
import threading
try:
    import queue
except ImportError:
    import Queue as queue

host = "127.0.0.1"


class SocketInjector:
    def verify_message(self, port1, port2, message, destination):
        q = queue.Queue()
        threading.Thread(target=open_connection, args=(port1, q)).start()

        send_message(port2, message, destination)
        return q.get()


def open_connection(port, q):
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conn.bind((host, port))
    socket_conn.listen(1)

    conn, _ = socket_conn.accept()
    payload = str(conn.recv(1024)).encode("utf-8")
    q.put(payload)


def send_message(port, message, destination):
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    payload = {
        "destination": destination,
        "message": message
    }

    dumped_message = bytes(json.dumps(payload).encode("UTF-8"))

    socket_conn.connect((host, port))
    socket_conn.sendall(dumped_message)


if __name__ == '__main__':
    injector = SocketInjector()
    print(injector.verify_message(3005, 3001, "test", "ENDPOINT"))
