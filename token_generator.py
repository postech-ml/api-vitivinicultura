from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token

api = Namespace('auth', description='Operações de autenticação')

model_login = api.model('Login', {
    'username': fields.String(required=True, description='Nome de usuário'),
    'password': fields.String(required=True, description='Senha')
})

@api.route('/create_token')
class TokenGenerator(Resource):
    @api.expect(model_login)
    def post(self):
        """Endpoint para realizar login e gerar token JWT"""
        username = request.json.get('username')
        password = request.json.get('password')

        # Verificação das credenciais (exemplo fixo para demonstração)
        if username == 'admin' and password == 'admin123':
            access_token = create_access_token(identity=username)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Usuário ou senha inválidos'}, 401
# api.add_resource(TokenGenerator, '/create_token')
