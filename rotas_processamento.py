from flask import jsonify
from flask_jwt_extended import jwt_required
from processamento import Processamento

class RotasProcessamento:
    @staticmethod
    def registrar_rotas(app):
        @app.route('/processamesa', methods=['GET'])
        @jwt_required()
        def processa_mesa():
            url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
            dados_json = Processamento.baixar_e_processar_csv(url)
            return jsonify(dados_json)

        @app.route('/processavinifera')
        @jwt_required()
        def processa_vinifera():
            url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
            dados_json = Processamento.baixar_e_processar_csv(url)
            return jsonify(dados_json)

        @app.route('/processaamericanas')
        @jwt_required()
        def processa_americanas():
            url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"
            dados_json = Processamento.baixar_e_processar_csv(url)
            return jsonify(dados_json)

        @app.route('/processasemclass')
        @jwt_required()
        def processa_sem_class():
            url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
            dados_json = Processamento.baixar_e_processar_csv(url)
            return jsonify(dados_json)