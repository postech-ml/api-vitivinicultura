from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

#tk = Flask(__name__)
#tk.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
#jwt = JWTManager(tk)


class TokenGenerator:
    @staticmethod
    def criar_token(app):
     app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
     jwt = JWTManager(app)
     @app.route('/login', methods=['POST'])
     def login():
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if username == 'usuario' and password == 'senha':
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Usuário ou senha inválidos'), 401

#if __name__ == "__main__":
    #tk.run(debug=True)