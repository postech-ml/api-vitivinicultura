from flask import jsonify
# from flask_jwt_extended import jwt_required
# from processamento import Processamento

# class RotasProcessamento:
#     @staticmethod
#     def registrar_rotas(app):
#         @app.route('/processamesa', methods=['GET'])
#         @jwt_required()
#         def processa_mesa():
#             url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
#             dados_json = Processamento.baixar_e_processar_csv(url)
#             return jsonify(dados_json)

#         @app.route('/processavinifera')
#         @jwt_required()
#         def processa_vinifera():
#             url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
#             dados_json = Processamento.baixar_e_processar_csv(url)
#             return jsonify(dados_json)

#         @app.route('/processaamericanas')
#         @jwt_required()
#         def processa_americanas():
#             url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"
#             dados_json = Processamento.baixar_e_processar_csv(url)
#             return jsonify(dados_json)

#         @app.route('/processasemclass')
#         @jwt_required()
#         def processa_sem_class():
#             url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
#             dados_json = Processamento.baixar_e_processar_csv(url)
#             return jsonify(dados_json)

from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from processamento import Processamento

api = Namespace('processamento', description='Operações de processamento')

class ProcessaMesa(Resource):
    @api.doc('processa_mesa')
    @api.response(200, 'Sucesso')
    @jwt_required()
    def get(self):
        """Processa dados da mesa"""
        url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
        dados_json = Processamento.baixar_e_processar_csv(url)
        return dados_json, 200

class ProcessaVinifera(Resource):
    @api.doc('processa_vinifera')
    @api.response(200, 'Sucesso')
    @jwt_required()
    def get(self):
        """Processa dados de vinifera"""
        url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
        dados_json = Processamento.baixar_e_processar_csv(url)
        return dados_json, 200

# Adiciona as rotas ao namespace
api.add_resource(ProcessaMesa, '/processamesa')
api.add_resource(ProcessaVinifera, '/processavinifera')

# A chamada para adicionar os recursos ao namespace deve ser removida daqui