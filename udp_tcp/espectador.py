import socket
import threading
import time
import subprocess
import os

# Função para receber mensagens do servidor
def assistir_jogo():
  msg_atualizacao = f"atualiza aê {(ip_udp, porta_udp)}"
  while(True):
    # Inicia uma thread para atualizar o jogo
    espectador_thread = threading.Thread(target=atualizar_jogo)
    espectador_thread.start()

    # solicita atualização para o servidor
    try:
      socket_udp.sendto(msg_atualizacao.encode('utf-8'), (ip_udp, porta_udp)) 
    except:
      print("erro de envio")
      # tenta conectar com outro ip 
      indice_ip += 1
      ip_espectador = ips[indice_ip]
      socket_udp.bind((ip_espectador, porta_espectador))
      continue
      
    # Aguarda um intervalo antes da próxima atualização
    time.sleep(5)

def atualizar_jogo():
  while True:
    try:
      msg, endereco_servidor = socket_udp.recvfrom(1024) 
      mensagem = msg.decode('utf-8') # mensagem do servidor
      os.system('cls')  # limpa tela
      t = time.localtime()
      agora = time.strftime("%H:%M:%S", t)
      print(f"Ultima atualização: {agora}, em {(ip_udp, porta_udp)}") # exibe momento da mensagem
      print(mensagem) # mensagem do servidor
    except:
      break

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

# Dados conexão UDP
ip_espectador = ip_local
porta_espectador = 4000
ip_udp = "10.25.3.121" # pegar endereco do servidor UDP
porta_udp = 5000
print(f"Endereço local ({ip_espectador}:{porta_espectador})")
print(f"Endereço servidor UDP ({ip_udp}:{porta_udp})")
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind((ip_espectador, porta_espectador)) # testar configuração de ip sugerida por gracon

assistir_jogo()
print("Cliente espectador iniciado.")

  

