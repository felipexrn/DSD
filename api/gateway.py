from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import requests
from flask_cors import CORS  # Importe a extensão CORS

app = Flask(__name__)
CORS(app)  # Adicione esta linha para habilitar o CORS
api = Api(app, version='1.0', title='RPG Gateway', description='API Gateway para rotear APIs de Rolagem de Dados e Modificador')

# Configuração das URLs das APIs subjacentes
ROLAGEM_API_URL = "http://localhost:5000/rolagem_de_dado"
MODIFICADOR_API_URL = "http://localhost:5001/rolagem_modificada"

# Modelo para a solicitação da API de rolagem_de_dado
rolagem_modelo = api.model('rolagem_de_dado', {
    'rolagem_de_dado': fields.Integer(description='Resultado da rolagem do dado')
})

# Modelo para a solicitação da API de modificador
modificador_modelo = api.model('rolagem_modificada', {
    'rolagem_modificada': fields.Integer(description='Resultado da modificação da rolagem')
})

# Crie um namespace com um nome personalizado
rpg_gateway_namespace = api.namespace('rpg_gateway', description='Rola Dados e modifica o resultado das rolagens.')

# Rota para a API Gateway que chama a API de rolagem de dados
#@api.route('/gateway/rolagem_de_dado/<int:quantidade>/<int:numero_lados>', methods=['GET'])
@rpg_gateway_namespace.route('/rolagem_de_dado/<int:quantidade>/<int:numero_lados>', methods=['GET'])
class APIGatewayRolagem(Resource):
    @api.doc(params={'quantidade': 'Número de vezes que o dado será rolado', 'numero_lados': 'Número de lados do dado'})
    @api.marshal_list_with(rolagem_modelo)
    def get(self, quantidade, numero_lados):
        """
        Rola um dado com o número especificado de lados uma determinada quantidade de vezes.
        parâmetro quantidade: O número de vezes que o dado será rolado.
        parâmetro numero_lados: O número de lados do dado.
        retorno: Lista de resultados das rolagens.
        """
        # Construa a URL da API subjacente
        url = f"{ROLAGEM_API_URL}/{quantidade}/{numero_lados}"
        # Faça a solicitação para a API subjacente
        response = requests.get(url)
        # Retorne a resposta da API subjacente para o cliente
        return response.json()

# Rota para a API Gateway que chama a API de modificador
#@api.route('/gateway/rolagem_modificada/<int:rolagem>/<int:modificador>', methods=['GET'])
@rpg_gateway_namespace.route('/rolagem_modificada/<int:rolagem>/<int:modificador>', methods=['GET'])
class APIGatewayModificador(Resource):
    @api.doc(params={'rolagem': 'Resultado da rolagem do dado', 'modificador': 'valor do modificador'})
    @api.marshal_list_with(modificador_modelo)
    def get(self, rolagem, modificador):
        """
        Modifica a rolagem de um dado por um valor de um modificador.
        parâmetro rolagem: O valor rolado no dado.
        parâmetro modificador: O número a ser adicionado como modificador.
        retorno: Valor modificado.
        """
         # Construa a URL da API subjacente
        url = f"{MODIFICADOR_API_URL}/{rolagem}/{modificador}"
        # Faça a solicitação para a API subjacente
        response = requests.get(url)
        # Retorne a resposta da API subjacente para o cliente
        return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5002)
