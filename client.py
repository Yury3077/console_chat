import socket
import threading

SIZE_PACKAGE = 65535


def listen(s: socket.socket):

    while True:
        data = s.recv(SIZE_PACKAGE)
        print("\r\r" + data.decode("utf-8") + "\n" + f"you: ", end="")


def connect(host: str, port: int):
    """
    Get connection with server and send input message from user
    :param host: IP address
    :param port: Number of port
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()
    name_or_id = input("Enter your name or ID: ")
    s.send(name_or_id.encode("utf-8"))

    while True:
        msg = input(f"you: ")
        s.send(msg.encode("utf-8"))


if __name__ == "__main__":
    print("Welcome to chat!")
    connect("127.0.0.1", 9090)
