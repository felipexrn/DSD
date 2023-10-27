import Pyro4
import pygame

uri = "PYRO:obj_ffe3676b73e34c289526fff6f86eeea4@localhost:58300"
grid = Pyro4.Proxy(uri)

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = grid.get_largura(), grid.get_altura()
tamanho_quadrado = grid.get_tamanho_quadrado()

# Altura da barra de seleção de cores
altura_barra_cores = tamanho_quadrado*2

# altura -= altura_barra_cores

# Cria a janela
janela = pygame.display.set_mode((largura, altura + altura_barra_cores))
pygame.display.set_caption("Trabalho de DSD")

# Cores
branco = (255, 255, 255)
cor_linha = (200, 200, 200)

#Cor padrão do usuário
cor_usuario = branco

#Prepara o palco para ser colorido
janela.fill(branco)

# Gera uma porção de cores possíveis para serem exibidas para seleção
cores_disponiveis = []  
for i in range(256):
    r = 255 - i
    g = i
    b = 0
    cor = (r, g, b)
    cores_disponiveis.append(cor)

for i in range(256):
    r = 0
    g = 255 - i
    b = i
    cor = (r, g, b)
    cores_disponiveis.append(cor)

for i in range(256):
    r = i
    g = 0
    b = 255 - i
    cor = (r, g, b)
    cores_disponiveis.append(cor)

largura_cor = largura // len(cores_disponiveis)

#Desenha a barra de seleção de cores
for i, cor in enumerate(cores_disponiveis):
    x_pos = i * largura_cor
    pygame.draw.rect(janela, cor, (x_pos, altura, largura_cor, altura_barra_cores))




linhas = grid.get_linhas()
colunas = grid.get_colunas()
if grid.get_posicoes() == []:
    grid.set_posicoes([[branco] * colunas for _ in range(linhas)])


tamanho_preview_cor = largura - (cores_disponiveis.__len__() * largura_cor )

# Loop principal
selecionando_cor = False
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if y >= altura: # Clicar além do tabuleiro (na barra de cores)
                cor_usuario = cores_disponiveis[x // largura_cor] if x <= largura-tamanho_preview_cor else branco
                selecionando_cor = True
            else:
                linha = y // tamanho_quadrado
                coluna = x // tamanho_quadrado

                if grid.get_posicao(linha, coluna) == branco:
                    grid.colorir(cor_usuario, linha, coluna)
                else:
                    grid.colorir(branco, linha, coluna)

        if evento.type == pygame.MOUSEBUTTONUP:
            selecionando_cor = False

    if selecionando_cor:
        pygame.draw.rect(janela, cor_usuario, (largura - tamanho_preview_cor, altura, tamanho_preview_cor, altura_barra_cores))

    posicoes_coloridas = grid.get_posicoes_coloridas()

    if posicoes_coloridas.__len__() > 0:
        for p in posicoes_coloridas:
            linha, coluna = p
            cor = grid.get_posicao(linha, coluna)
            pygame.draw.rect(janela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))
            # pygame.draw.rect(janela, cor_linha, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado), 1)

    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
