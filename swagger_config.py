from rotas_processamento import api as ns_rotas_processamento
from token_generator import api as ns_token_generator
class SwaggerConfig:
    @staticmethod
    def configurar(api):
        api.title = 'Viti Vinicultura'
        api.version = '1.0'
        api.description = 'API da Viti Vinicultura'
        # Cria uma instância da API com a configuração do Swagger
        # api = Api(app, version='1.0', title='API de Exemplo', description='Uma API de exemplo com Swagger')

        # Aqui você pode adicionar namespaces ou modelos
        # Por exemplo: api.add_namespace(ns_processamento, path='/processamento')
        api.add_namespace(ns_token_generator, path='/login')
        api.add_namespace(ns_rotas_processamento, path='/processamento')
        
        return api

 