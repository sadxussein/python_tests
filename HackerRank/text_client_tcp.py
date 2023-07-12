import socket

# установить IP-адрес и порт сервера
SERVER_HOST = '192.168.1.123'
SERVER_PORT = 55055

# создать сокет и подключиться к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    # получить ввод от пользователя
    message = input("Введите сообщение: ")

    # отправить сообщение серверу
    client_socket.send(message.encode())

    # получить ответ от сервера
    response = client_socket.recv(1500).decode()

    # вывести ответ на экран
    print("Ответ сервера:", response)

    # выйти из цикла при вводе пустой строки
    if not message:
        break

# закрыть соединение
client_socket.close()