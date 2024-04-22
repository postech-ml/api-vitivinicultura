from flask_restx import Api
from rotas_processamento import api as ns_processamento

class SwaggerConfig:
    @staticmethod
    def configurar(api):
        api.title = 'API de Exemplo'
        api.version = '1.0'
        api.description = 'Uma API de exemplo com Swagger'
        # Cria uma instância da API com a configuração do Swagger
        # api = Api(app, version='1.0', title='API de Exemplo', description='Uma API de exemplo com Swagger')

        # Aqui você pode adicionar namespaces ou modelos
        # Por exemplo: api.add_namespace(ns_processamento, path='/processamento')
        api.add_namespace(ns_processamento, path='/processamento')
        return api

 