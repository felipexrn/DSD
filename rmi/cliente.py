import Pyro4

# URI do objeto retângulo (substitua com a URI real)
#uri = "PYRO:obj_id@localhost:50583"
uri = "PYRO:obj_4d9c96aea3d74ba4a89b93f068d837fa@localhost:50646"
# Conecta-se ao objeto remoto
retangulo = Pyro4.Proxy(uri)
retangulo.set_base(5)
retangulo.set_altura(3)
# Chama o método calcular_area remotamente
area = retangulo.calcular_area()
print(f"Área do retângulo: {area}")
print(retangulo.imprimir())