import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
print(f'Servidor rodando no endereço: ${server_address}')
sock.bind(server_address)
sock.listen(1)

while True:
    print('esperando conexão')
    connection, client_address = sock.accept()
    try:
        print('Conexão de', client_address)

        # Recebe a informação e devolve uma resposta ao cliente
        data = connection.recv(16)
        data = data.decode("utf-8")
        if data == 'Hello, world!':
            print(f'recebido: {data}')
            print('enviando mensagem de volta para o cliente')
            data = 'Hello,From TCP!'
            connection.sendall(data.encode("utf-8"))
            break
        else:
            print(f'recebido: ${data}')
            print('enviando mensagem de volta para o cliente')
            data = 'errou a senha'
            connection.sendall(data.encode("utf-8"))
            print('sem mais mensagens de', client_address)
            break 
    finally:
        # Clean up the connection
        connection.close()