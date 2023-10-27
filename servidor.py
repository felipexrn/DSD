import Pyro4
from grid import Grid

# Inicialização do Pyro4
daemon = Pyro4.Daemon()

# Instanciar a classe Grid no servidor
grid = Grid(800, 600, 20)
uri = daemon.register(grid)
print(f"{uri}")

# Registrar o objeto no Nameserver

daemon.requestLoop()
