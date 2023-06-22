import socket

SERVER_ADDRESS = ('192.168.1.123', 55056)

# создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # отправляем данные серверу
    message = input("Введите сообщение: ")
    
    client_socket.sendto(message, SERVER_ADDRESS)

    # получаем ответ от сервера
    data, server_address = client_socket.recvfrom(1500)
    print(f"Received '{data.decode()}' from {server_address}")
    
    # выйти из цикла при вводе пустой строки
    if not message:
        break

# закрываем сокет
client_socket.close()