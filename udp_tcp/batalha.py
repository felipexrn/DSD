import random
import os

class Partida:
  def __init__(self, id_partida):
    self.id_partida = id_partida
    self.turno = 0
    self.status = 'espera'  # 'encerrada', 'espera' ou 'ativa'
    self.resultado = ''  # 'p1', 'p2' ou 'empate'
    self.jogadores = []  # Lista de objetos Jogador
    self.jogadas = []  # Lista de objetos Jogada
    self.campos = [] # Lista de objetos Campo

  def adicionar_jogador(self, Jogador):
    self.jogadores.append(Jogador)
    self.campos.append(Campo())

  def validar_jogada(self, ataque_jogador, campo_oponente):
    comando_valido = True
    if len(ataque_jogador) != 2: comando_valido = False
    elif ataque_jogador[0].upper() not in campo_oponente.colunas: comando_valido = False
    elif ataque_jogador[1] not in campo_oponente.linhas: comando_valido = False
    if not comando_valido:
      fi = "\033[1;31m"
      ff = "\033[0m"
      print(f"{fi}Comando inválido: {ataque_jogador}{ff}")
      print(f"Envie somente as cordenadas no formato de letra e número. Exemplo: {campo_oponente.colunas[random.randrange(campo_oponente.col)]}{campo_oponente.linhas[random.randrange(campo_oponente.lin)]}")
      print(f"Envie coordenadas dentro do intervalo: {campo_oponente.colunas[0]}{campo_oponente.linhas[0]} até {campo_oponente.colunas[-1]}{campo_oponente.linhas[-1]}")
    return comando_valido

  def adicionar_jogada(self, jogada):
    self.jogadas.append(jogada)
        

class Jogador:
  def __init__(self, ip, porta, nome):
    self.ip = ip
    self.porta = porta
    self.nome = nome
    

class Jogada:
  def __init__(self, jogador, partida, x, y):
    self.jogador = jogador  # Objeto Jogador
    self.partida = partida
    self.x = ord(x) - 65
    self.y = y-1
    
    
  def confere(self, campo):
    fi = "\033[1;32m"
    ff = "\033[0m"
    s = fi
    s += f"{chr(self.x + 65)}{self.y}"
    if campo.campo[self.y][self.x] == campo.char_navio:
      print(s, "kabum", ff)
      campo.campo[self.y][self.x] = campo.char_acerto
    elif campo.campo[self.y][self.x] == campo.char_vazio:
      print(s, "água", ff)
      campo.campo[self.y][self.x] = campo.char_agua
    else:
      print(s, "De novo?", ff)


class Campo:
  def __init__(self):
    # dados do campo
    self.tam = 5
    self.col = self.tam
    self.lin = self.tam
    self.navios = 5
    self.char_navio = "N"
    self.char_vazio = "_"
    self.char_acerto = "X"
    self.char_agua = "A"
    self.campo = []
    self.colunas = []
    self.linhas = [str(i) for i in range(1, self.lin +1)]
    self.criar()
    self.popular()
  
  def criar(self):
    # cria o campo
    for i in range(self.lin):
      self.campo.append([self.char_vazio] * self.col)
      
    # cria cabeçalho das colunas do campo
    for i in range(self.col):
      self.colunas.append(chr(i + 65))

  def popular(self):
      # popula campo com navios
    n = self.navios
    while(n>0):
      x = random.randrange(self.col)
      y = random.randrange(self.lin)
      if self.campo[y][x] != self.char_navio:
        self.campo[y][x] = self.char_navio
        n -= 1

  def str_campo(self, tipo):
    # transforma campo em string
    s = ""
    
    # cabeçalho das colunas
    s += " "
    for i in self.colunas:
      s += " " + i
    s += "\n"
    
    # imprime linhas 
    i = 1
    for l in self.campo:
      s += str(i)
      for c in l:
        # 1 = Jogador, 2 = Oponente 
        if (tipo == 2) and (c == self.char_navio):
          s += " " + self.char_vazio
        else:
          s += " " + c
      i+=1
      s+= "\n"
    return s


# teste da partida

# cria partida com ID
p1 = Partida(1)

# cria jogadores
jj1 = Jogador(ip="127.0.0.1", porta=5000, nome="Fulano")
jj2 = Jogador(ip="127.0.0.1", porta=5001, nome="Beltrano")

# adiciona jogadores à partida e cria um campo para cada
p1.adicionar_jogador(jj1)
p1.adicionar_jogador(jj2)

# exibe tela inicial da partida
os.system('clear')  # limpa tela
print(f"Campo jogador2: {p1.jogadores[1].nome}\n")
print(p1.campos[1].str_campo(2))
print("---------------------\n")
print(f"Campo jogador1: {p1.jogadores[0].nome}\n")
print(p1.campos[0].str_campo(1))

# testa N jogadas do jogador1
for i in range(30):
  x = chr(random.randrange(7) + 65)
  y = random.randrange(1,8)
  if p1.validar_jogada(x+str(y), p1.campos[1]): 
    j1 = Jogada(p1.jogadores[0], 1, x,y)
    p1.adicionar_jogada(j1)
    j1.confere(p1.campos[1])

# exibe tela final da partida
print(f"Campo jogador2: {p1.jogadores[1].nome}\n")
print(p1.campos[1].str_campo(2))
print("---------------------\n")
print(f"Campo jogador1: {p1.jogadores[0].nome}\n")
print(p1.campos[0].str_campo(1))