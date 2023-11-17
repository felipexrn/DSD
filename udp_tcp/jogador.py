import socket
import threading

turno = 0
#id_partida = ""
nome_jogador = ""
nome_oponente = ""

# Função para envio de mensagens ao servidor
def jogada(socket_jogador, nome_jogador):
    
  print(f"Jogador {nome_jogador} ({jogador.ip}) conectado à Partida {partida.id_partida}")
    

  # Exemplo: receber mensagens do jogador
  while True:
    mensagem_servidor = socket_jogador.recv(1024).decode('utf-8')
    if not mensagem:
      break
    nome_oponente = mensagem_servidor[0]
    oponente_ip = mensagem_servidor[0]
    jogada_oponente = mensagem_servidor[0]
    campo_jogador = mensagem_servidor[0]
    print(f"Jogador {nome_oponente} ({oponente_ip}) jogou: {jogada_oponente}")
    print(campo_oponente)
    print(campo_jogador)

# Configura conexão com o servidor TCP
tcp_ip = '127.0.0.1' # pegar endereco do servidor TCP
porta_tcp = 12345
socket_jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_jogador.connect((tcp_ip, porta_tcp));

# Inscreve jogador na partida
print("Digite seu nome de jogador")
nome_jogador = input() # nome de jogador
#print("Digite ID da partida")
#id_partida = input() # id_partida
#print(f"O ID da partida é {id_partida}")

socket_jogador.send(nome_jogador.encode('utf-8'));
mensagem_servidor = socket_jogador.recv(1024).decode('utf-8')
print(mensagem_servidor)

while True:
  thread = threading.Thread(target=jogada, args=(socket_jogador, nome_jogador))
  thread.start()

# veja estes sites:
  '''
  https://pythontic.com/modules/socket/send
  https://wiki.python.org/moin/UdpCommunication
  '''