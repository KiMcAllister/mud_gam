import socket
import select



print("Welcome to our server app, if you answer a few questions we will have your campain up in a jiffy!")

header_len = 10
server_ip = "0.0.0.0"
server_port = int(input("What port would you like host your server on? (i.e. 5555)\n> "))

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.bind((server_ip, server_port))
server_connection.listen()

player_connections = [server_connection]

player_info = {}


def get_player_input(player_connection):
    try:
        input_header = player_connection.recv(header_len)
        if len(input_header) == 0:
            return False
        return {'header' : input_header, 'data' : player_connection.recv(int(input_header))}
    except:
        return False


while True:
    socket_test, _, errors = select.select(player_connections, [], player_connections)

    for s in socket_test:
        if s == server_connection:
            joining_connection, joining_address = server_connection.accept()
        
            test = get_player_input(joining_connection)
            if test is False:
                continue

            player_connections.append(joining_connection)
            player_info[joining_connection] = test

            print("Player {} just joined from {}:{}".format(test['data'].decode(),*joining_address))
        else:
            message = get_player_input(s)
            if message is False:
                print("Player: {} has been disconnected".format(player_info[s]['data'].decode()))
                player_connections.remove(s)
                del player_info[s]
                continue

            user = player_info[s]
            print("player {} has given the command: {}".format(user['data'],message['data'].decode()))
            for player in player_info:
                #if player != s:
                    player.send(user['header']+user['data']+message['header']+message['data'])


    for s in errors:
        player_connections.remove(s)
        del player_info[s]
