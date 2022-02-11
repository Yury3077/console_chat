import socket

SIZE_PACKAGE = 65535


def listen(host: str, port: int):
    """
    Waiting for data from client in a port and send to others
    :param host: IP address
    :param port: Number of port
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print(f"Listening {host}:{port}")

    users = {}
    while True:
        data, addr = s.recvfrom(SIZE_PACKAGE)

        if addr not in users.keys():
            users[addr] = data
            print(f'Client {data.decode("utf-8")} joined chat')
        else:
            msg_to_chat = f'{users[addr].decode("utf-8")}: {data.decode("utf-8")}'
            for user in users.keys():
                if user[1] == addr[1]:
                    continue
                s.sendto(msg_to_chat.encode("utf-8"), user)


if __name__ == "__main__":
    listen("127.0.0.1", 9090)
