import Pyro4

@Pyro4.expose
class Grid:
    def __init__(self, largura, altura, tamanho_quadrado):
        self.largura = largura
        self.altura = altura
        
        self.tamanho_quadrado = tamanho_quadrado
        self.linhas = altura // tamanho_quadrado
        self.colunas = largura // tamanho_quadrado
        self.posicoes = []
        self.posicoes_coloridas = []

    def get_posicao(self, x, y):

        return self.posicoes[x][y]
    
    def set_posicao(self, x, y, cor):
        self.posicoes[x][y] = cor

    def atualizar_cor_quadrado(self, linha, coluna, cor):
        self.posicoes[linha][coluna] = cor
    
    def get_largura(self):
        return self.largura
    
    def get_altura(self):
        return self.altura
    
    def get_tamanho_quadrado(self):
        return self.tamanho_quadrado
    
    def set_posicoes(self, m):
        self.posicoes = m
    
    def get_posicoes(self):
        return self.posicoes
    
    def get_linhas(self):
        return self.linhas

    def get_colunas(self):
        return self.colunas
    
    def colorir(self, cor, linha, coluna):
        
        self.posicoes[linha][coluna] = cor
        self.posicoes_coloridas.append((linha, coluna))
       


    def get_posicoes_coloridas(self):
        return self.posicoes_coloridas