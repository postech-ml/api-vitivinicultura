from flask import Flask
from swagger import Swagger
from token_generator import TokenGenerator
from rotas_processamento import RotasProcessamento


app = Flask(__name__)

# Chamar o método criar_token da classe TokenGenerator
TokenGenerator.criar_token(app)

# Registrar as rotas de processamento
RotasProcessamento.registrar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)
    Swagger.registrar_rotas(Flask(__name__))
    Swagger.run()