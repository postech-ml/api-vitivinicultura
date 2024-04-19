import pandas as pd
import requests
from io import StringIO 
import json

class Processamento:
    @staticmethod
    def baixar_e_processar_csv(url):
        resposta = requests.get(url)
        resposta.encoding = 'utf-8' 
        resposta.raise_for_status()  # Lança um erro para respostas não bem-sucedidas
        #dados = pd.read_csv(StringIO(resposta.text))  # Modifique esta linha
        dados = pd.read_csv(StringIO(resposta.text), sep="\t")
        #dados.to_clipboard()
       
        resultado_final_= dados.to_json(orient="records")
        return json.loads(resultado_final_)