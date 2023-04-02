import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello From UDP Server"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Conectando ao Adress e ao IP
UDPServerSocket.bind((localIP, localPort))
print("UDP server online esperando cliente...")

# Espera pelo cliente
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print(f'Mensagem do cliente: {message}')
    print(f'Endereço IP do cliente: {address}')
    # Resposta ao cliente
    UDPServerSocket.sendto(bytesToSend, address)
