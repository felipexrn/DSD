import Pyro4
from grid import Grid

# Inicialização do Pyro4
daemon = Pyro4.Daemon()

# Instanciar a classe Grid no servidor
grid = Grid(900, 1000, 20)

# Registra o objeto remoto no servidor de nomes
ns = Pyro4.locateNS()
uri = daemon.serveSimple(
    {
        grid: "canva"
    },
    host='localhost',
    port=9091
)
ns.register("canva", uri)
print(uri)

# Inicia o servidor rmi
daemon.requestLoop()
