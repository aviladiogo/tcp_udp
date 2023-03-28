import socket
from time import sleep

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conexão com o server
server_address = ('localhost', 8080)
print(f'se conectando a porta {server_address[1]}')
sock.connect(server_address)

try:   
    # enviando mensagem, ela precisa estar codificada em bytes,  string não pode ser enviado
    message = 'Hello, world!'
    print(f'enviando {message} para o server')
    sock.sendall(message.encode("utf-8"))

    # esperando resposta do server, e decodificando a mensagem
    sleep(3)
    data = sock.recv(16)
    data = data.decode("utf-8")
    print(f'recebido: {data}')
finally:
    print('fechando socket')
    sock.close()