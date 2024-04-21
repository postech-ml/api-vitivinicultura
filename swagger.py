import resource
from flask import Flask
from flask_restx import Api, Resource
from rotas_processamento import RotasProcessamento

class Swagger:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, version='1.0', title='API de Exemplo', description='Descrição da API')
        api = Api(self.app)
        @api.route('/hello')
        class HelloWorld(Resource):
         def get(self):
          return {'hello': 'world'}
        # Registrar as rotas do arquivo rotas_processamento.py
        RotasProcessamento.registrar_rotas(self.app)

 