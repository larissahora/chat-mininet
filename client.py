import socket
import time
    
def discover_servers():
    ENDERECO_BROADCAST = '10.0.0.255'
    PORTA_BROADCAST = 5000
    mensagem_broadcast = "Sonda"
    
    servers = []
    
    # Configuração do socket UDP
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Enviar sonda broadcast
    for _ in range(3):
        udp.sendto(mensagem_broadcast.encode('utf-8'), (ENDERECO_BROADCAST, PORTA_BROADCAST))
        print(f"Sonda enviada para {ENDERECO_BROADCAST}:{PORTA_BROADCAST}")
        time.sleep(1)
    
        # Configuração do timeout para recepção de respostas
        udp.settimeout(1)
    
    try:
        while True:
            data, addr = udp.recvfrom(1024)
            server_ip = addr[0]
            print(f"Servidor encontrado: {server_ip}")
            servers.append(server_ip)
    except socket.timeout:
            pass
    
    udp.close()
    return servers
    
def choose_server(servers):
    print("Servers disponíveis: ")
    for i, server in enumerate(servers):
        print(f"{i + 1}. {server}")
    
    choice = int(input(f"Escolha um servidor para se conectar (1-{len(servers)}): "))
    if 1 <= choice <= len(servers):
        return servers[choice - 1]
    else:
        print("Escolha inválida. Tchau.")
        exit()
    
def connect_to_server(server_ip):
    PORTA_TCP = 5001  
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((server_ip, PORTA_TCP))
    print(f"Conectado ao servidor em {server_ip}")
    return tcp_socket
    
if __name__ == '__main__':
    servers = discover_servers()
    chosen_server = choose_server(servers)
    server_socket = connect_to_server(chosen_server)
    
    while True:
        message = input("Cliente: ")
        server_socket.sendall(message.encode('utf-8'))
            
        mensagem_recebida_tcp = server_socket.recv(1024).decode('utf-8')
        print(f"Server: {mensagem_recebida_tcp}")