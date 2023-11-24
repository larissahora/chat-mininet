# Aplicação de chat no mininet

Este projeto opera em uma topologia circular, onde 6 hosts estão conectados em 4 switchs e todos eles conseguem se enxergar através do Spanning Tree Protocol (STP).   

## Funcionamento

Em ambiente mininet, comece rodando a topologia   
```sudo python topology.py```   

Execute na quantidade desejada, um xterm para cada host   
```xterm h1 h2 h3 h4```  

Escolha os servidores e execute o script   
```sudo python server.py```

No cliente, execute   
```sudo python client.py```  

E comece a conversar 🤓
