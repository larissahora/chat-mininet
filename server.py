import socket

IP_SERVIDOR = ''         # Endereço IP do Servidor
PORTA_UDP = 5000           # Porta UDP que o Servidor vai ouvir
PORTA_TCP = 5001           # Porta TCP que o Servidor vai ouvir

# Configurando o socket UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVIDOR_UDP = (IP_SERVIDOR, PORTA_UDP)
udp.bind(SERVIDOR_UDP)       # Faz o bind do IP e da porta UDP para começar a ouvir

print(f"Servidor UDP ouvindo em {PORTA_UDP}")

# Recebe a mensagem UDP (sonda)
mensagem_sonda, endereco_cliente_udp = udp.recvfrom(1024)
ip_cliente, porta_cliente = endereco_cliente_udp

print(f"Sonda: {mensagem_sonda}")

# Envia mensagem de disponibilidade ao cliente UDP
mensagem_disponivel = 'Disponivel'
udp.sendto(mensagem_disponivel.encode('utf-8'), (ip_cliente, porta_cliente))

# Configurando o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MEU_SERVIDOR_TCP = (IP_SERVIDOR, PORTA_TCP)
tcp.bind(MEU_SERVIDOR_TCP)       # Faz o bind do IP e da porta TCP para começar a ouvir
tcp.listen(1)  # Limita o número de conexões pendentes a 1

# Aceita conexão TCP
print(f"Servidor TCP ouvindo em {PORTA_TCP}")
tcp_connection, tcp_address = tcp.accept()
print(f"Conexão TCP estabelecida com {tcp_address}")

while True:
    # Recebe a mensagem TCP
    mensagem_recebida_tcp = tcp_connection.recv(1024).decode('utf-8')
    if not mensagem_recebida_tcp:
        break  # Se a conexão TCP for encerrada, saia do loop

    print(f"Cliente: {mensagem_recebida_tcp}")

    # Envia a mensagem TCP
    mensagem_para_enviar = input("Servidor: ")
    tcp_connection.sendall(mensagem_para_enviar.encode('utf-8'))
    

# Fecha os sockets
tcp_connection.close()
tcp.close()
udp.close()
