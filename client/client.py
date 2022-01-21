import socket
import select
import errno
import sys

header_len = 10

print("Welcome to \"game name\" to get stated we need to connect you to your campaign")

server_ip = input("What is your campaign ip?\n> ")
server_port = int(input("What is your campaign port?\n> "))
username = input("What do you want your username to be?\n> ")

player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player_socket.connect((server_ip,server_port))
player_socket.setblocking(False)

username = username.encode()
username_header = f"{len(username):<{header_len}}".encode()

player_socket.send(username_header + username)

def send_input(text):
    text = f"{len(text):<{header_len}}".encode() + text.encode()
    player_socket.send(text)

def get_text():
    try:
        while True:
            username_header = player_socket.recv(header_len)

            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode())

            username = player_socket.recv(username_length).decode()

            message_header = player_socket.recv(header_len)
            message_length = int(message_header.decode())
            message = player_socket.recv(message_length).decode()
            return (f'{username} > {message}')
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error1: {}'.format(str(e)))
            sys.exit()
    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: {}'.format(str(e)))
        sys.exit()
