import Pyro4

# classe O Desenhista
@Pyro4.expose
class Canva:
    def __init__(self):
        self.altura
        self.largura
        self.canva 

# Classe do objeto Retângulo
@Pyro4.expose
class Retangulo:
    def __init__(self):
        self.base
        self.altura

    def calcular_area(self):
        return self.base * self.altura

    def set_base(self, b):
        self.base = b

    def set_altura(self, a):
        self.altura = a

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def imprimir(self):
        s = ""
        o = "o "

        # linha superior 
        for i in range(self.base):
            s += o
        s += "\n"

        # linhas internas
        for i in range(self.altura-2):
            s += o
            for i in range(self.base-2):
                s += "  "
            s += o + "\n"

        # linha inferior
        if self.altura>1: 
            for i in range(self.base):
                s += o
        
        return s

# Cria um objeto Retângulo
retangulo = Retangulo()

# Inicializa o daemon Pyro
daemon = Pyro4.Daemon()

# Registra o objeto Retângulo com um nome
uri = daemon.register(retangulo)
print(f"URI do objeto: {uri}")

# Inicia o servidor
daemon.requestLoop()