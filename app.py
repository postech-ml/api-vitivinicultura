from flask import Flask
from flask_restx import Api
from swagger_config import SwaggerConfig
from token_generator import TokenGenerator
from rotas_processamento import api as processamento_api

app = Flask(__name__)
api = Api(app)
SwaggerConfig.configurar(api)
# Swagger(app)
# Chamar o método criar_token da classe TokenGenerator
TokenGenerator.criar_token(app) 

# Registrar as rotas de processamento
# RotasProcessamento.registrar_rotas(app)
api.add_namespace(processamento_api) 

if __name__ == "__main__":
    app.run(debug=True)
   