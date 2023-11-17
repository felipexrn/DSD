import socket
import threading
import time
import subprocess
import os

# Função para lidar com a conexão de um jogador
def turno(socket_jogador, nome_jogador):
  mensagem_jogador = f"{nome_jogador} envie coordenadas de ataque usando letra e número. Exemplo: A5"
  atualiza_jogo = "Campo de batalha"
  # Implemente a lógica do jogo aqui
  if nome_jogador != '':
    while True:
      # atualiza espectadores
      msg, endereco_espectador = servidor_udp.recvfrom(1024)
      if (msg != None) and endereco_espectador != None:
        print(msg.decode('utf-8'))
        print(endereco_espectador)
        try:
          servidor_udp.sendto(atualiza_jogo.encode('utf-8'), endereco_espectador) 
        except:
          indice_ip += 1
          ip_local = ips[indice_ip]
          ip_udp = ips[indice_ip]
          ip_tcp = ips[indice_ip]
          servidor_udp.bind((ip_udp, porta_udp))
          servidor_tcp.bind((ip_tcp, porta_tcp))
          continue
      #socket_jogador.send(mensagem_jogador.encode('utf-8')) # tcp

      # aguarda mensagem dos jogadores 
      #socket_jogador, ip_jogador = servidor_tcp.accept()
      #ataque_jogador = socket_jogador.recv(1024).decode('utf-8')

      # implemente o jogo aqui

# pega ipv4 do local
proc = subprocess.Popen('ipconfig | findstr /i "ipv4"', stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
ip_local = [chr(c) for c in out]
ips = []
indice_ip = 0
c = ip_local.count(':')
for ip in range(c):
  i = ip_local.index(":")+2
  f = ip_local.index("\r")
  ips.append("".join(ip_local[i:f]))
  ip_local = ip_local[f+1:]
ip_local = ips[indice_ip]

# Configuração do servidor UDP
ip_udp = ip_local
porta_udp = 5000
print(f"Servidor UDP iniciado em ({ip_udp}:{porta_udp}). Espectadores podem assitir partidas")
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_udp.bind((ip_udp, porta_udp))

# Configuração do servidor TCP
ip_tcp = ip_local
porta_tcp = 3000
servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_tcp.bind((ip_tcp, porta_tcp))
servidor_tcp.listen(2)  # Escuta dois jogadores
print(f"Servidor TCP iniciado em ({ip_tcp}:{porta_tcp}). Aguardando jogadores...")

# configura a thread
udp_thread = threading.Thread(target=turno, args=(0, "Fulano"))

# inicia a thread
udp_thread.start()


'''
# Espera dois jogadores se conectarem
jogadores = []
while len(players) < 2:
  socket_jogador, endereco_jogador = servidor_tcp.accept()
  nome_jogador = socket_jogador.recv(1024).decode('utf-8')
  print(f"Jogador {nome_jogador} conectado de {endereco_jogador}")
  players.append((socket_jogador, nome_jogador))
  socket_jogador.send("Você está conectado ao servidor!".encode('utf-8'));
  
# Inicia uma thread para cada jogador
threads = []
for socket_jogador, nome_jogador in jogadores:
  thread = threading.Thread(target=turno, args=(socket_jogador, nome_jogador))
  threads.append(thread)
  thread.start()

# Aguarda as threads terminarem
for thread in threads:
  thread.join()

# Fecha o servidor TCP
servidor_tcp.close()
servidor_udp
'''