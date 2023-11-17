# pip install zeep
from zeep import Client

url = 'http://localhost:8000/?wsdl'
cliente = Client(url)

nome = input("Digite seu nome: ")
resposta = cliente.service.ola(nome)
print(resposta)

ping = cliente.service.ping()
print(resposta)

a = input("Digite a: ")
resposta = cliente.service.ola(nome)
print(resposta)

while True:
    resposta = cliente.service.servicos_disponiveis()
    print(resposta)
    input("escolha um serviço")