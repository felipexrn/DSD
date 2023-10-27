import Pyro4
import pygame

uri = "<inserir_URI_gerada_pelo_servidor.py>"

grid = Pyro4.Proxy(uri)
# Inicializa o Pygame
pygame.init()


# Configurações da janela
largura, altura = grid.get_largura(), grid.get_altura()
tamanho_quadrado = grid.get_tamanho_quadrado()

# Cria a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Trabalho de DSD")

# Cores
branco = (255, 255, 255)
preto = (200, 200, 200)
azul = (0, 0, 255)


janela.fill(branco)

# Desenha o grid de quadrados com as linhas pretas
for linha in range(0, altura, tamanho_quadrado):
    pygame.draw.line(janela, preto, (0, linha), (largura, linha))
for coluna in range(0, largura, tamanho_quadrado):
    pygame.draw.line(janela, preto, (coluna, 0), (coluna, altura))


# Grid de cores
linhas = altura // tamanho_quadrado
colunas = largura // tamanho_quadrado
grid.set_posicoes([[branco] * colunas for _ in range(linhas)])

# Conjunto para armazenar as posições dos quadrados modificados
quadrado_modificado = None

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x, y = pygame.mouse.get_pos()
            linha = y // tamanho_quadrado
            coluna = x // tamanho_quadrado
            grid.set_posicao(linha, coluna, azul if grid.get_posicao(linha, coluna) == branco else branco) 
                
            quadrado_modificado = (linha, coluna)

                
    #Isso aqui precisa ser muito otimizado
    for linha in range(grid.get_linhas()):
        for coluna in range(grid.get_colunas()):
            cor = grid.get_posicao(linha, coluna)
            pygame.draw.rect(janela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))
            pygame.draw.rect(janela, preto, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado), 1)
            
    pygame.display.flip() 

# Encerra o Pygame
pygame.quit()