from flask import Flask
from flask_restx import Api
from swagger_config import SwaggerConfig
# from rotas_processamento import api as processamento_api
# from token_generator import api as token_api
from flask_jwt_extended import JWTManager
# from token_generator import TokenGenerator
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Defina sua chave secreta aqui
jwt = JWTManager(app)
api = Api(app)

#TokenGenerator.generate_token(app)
# app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_jwt'  
# jwt = JWTManager(app)

SwaggerConfig.configurar(api)
#api.add_namespace(token_api)
#api.add_namespace(processamento_api) 


if __name__ == "__main__":
    app.run(debug=True)
   