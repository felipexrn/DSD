from flask import Flask
from flask_restx import Api, Resource, fields
import random

app = Flask(__name__)
api = Api(app, version='1.0', title='Modificador', description='Uma API para modificar rolagens.')

# Defina o modelo para a resposta da API
resultado_modelo = api.model('Rolagem_modificada', {
    'rolagem_modificada': fields.Integer(description='Resultado da modificação da rolagem')
})

# Crie um namespace com um nome personalizado
rolagem_de_dado = api.namespace('rolagem_modificada', description='Modifica a rolagem de um dado por um valor de um modificador.')


# Rota para rolar o dado
#@api.route('/rolagem_modificada/<int:rolagem>/<int:modificador>')
@rolagem_de_dado.route('/<int:rolagem>/<int:modificador>')
class rolagem_modificada(Resource):
    @api.doc(params={'rolagem': 'Resultado da rolagem do dado', 'modificador': 'valor do modificador'})
    @api.marshal_list_with(resultado_modelo)
    def get(self, rolagem, modificador):
        """
        Modifica a rolagem de um dado por um valor de um modificador.
        parâmetro rolagem: O valor rolado no dado.
        parâmetro modificador: O número a ser adicionado como modificador.
        retorno: Valor modificado.
        """
        resultado = int(rolagem) + int(modificador)
        return {'rolagem_modificada': resultado}

if __name__ == '__main__':
    app.run(debug=True, port=5001)