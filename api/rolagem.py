from flask import Flask
from flask_restx import Api, Resource, fields
import random

app = Flask(__name__)
api = Api(app, version='1.0', title='Rolagem de Dado', description='Uma API para rolar dados.')

# Defina o modelo para a resposta da API
rolagem_modelo = api.model('rolagem_de_dado', {
    'rolagem_de_dado': fields.Integer(description='Resultado da rolagem do dado')
})

# Crie um namespace com um nome personalizado
rolagem_namespace = api.namespace('rolagem_de_dado', description='Rola um dado com o número especificado de lados uma determinada quantidade de vezes.')

# Rota para rolar o dado
#@api.route('/rolagem_de_dado/<int:quantidade>/<int:numero_lados>')
@rolagem_namespace.route('/<int:quantidade>/<int:numero_lados>')
class rolagem_de_dado(Resource):
    @api.doc(params={'quantidade': 'Número de vezes que o dado será rolado', 'numero_lados': 'Número de lados do dado'})
    @api.marshal_list_with(rolagem_modelo)
    def get(self, quantidade, numero_lados):
        """
        Rola um dado com o número especificado de lados uma determinada quantidade de vezes.
        parâmetro quantidade: O número de vezes que o dado será rolado.
        parâmetro numero_lados: O número de lados do dado.
        retorno: Lista de resultados das rolagens.
        """
        resultados = [random.randint(1, numero_lados) for _ in range(quantidade)]    
        return [{'rolagem_de_dado': resultado} for resultado in resultados]

    @api.doc(params={'quantidade': 'Número de vezes que o dado será rolado', 'numero_lados': 'Número de lados do dado'})
    @api.marshal_list_with(rolagem_modelo)
    def post(self, quantidade, numero_lados):
        """
        Rola um dado com o número especificado de lados uma determinada quantidade de vezes.
        parâmetro quantidade: O número de vezes que o dado será rolado.
        parâmetro numero_lados: O número de lados do dado.
        retorno: Lista de resultados das rolagens.
        """
        resultados = [random.randint(1, numero_lados) for _ in range(quantidade)]
        return [{'rolagem_de_dado': resultado} for resultado in resultados]

if __name__ == '__main__':
    app.run(debug=True, port=5000)