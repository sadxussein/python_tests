import socket
import msvcrt

SERVER_ADDRESS = ('192.168.1.123', 55056)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Считываем один символ ввода
    if msvcrt.kbhit():
        message = msvcrt.getch().decode('utf-8')
        client_socket.sendto(message.encode(), SERVER_ADDRESS)
        data, server_address = client_socket.recvfrom(1500)
        print(data)
        if message == 'q':
            break 

# закрываем сокет
client_socket.close()