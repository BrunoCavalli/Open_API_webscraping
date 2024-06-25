"""Modulo de implementação da API da openai"""

import pandas as pd
from openai import OpenAI

# inicializar o cliente OpenAI com a chave da API
chave_api = input("digite sua chave aqui:")
client = OpenAI(api_key=chave_api)

def analyze_data(dados_path):
    # ler o arquivo CSV
    dados = pd.read_csv(dados_path)
    dados_str = dados.to_string()
    
    # fazer a chamada para a API do openai
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
                "content": "You will be provided with a csv file, and your task is to make comments about the relation of the number of opinions and the value of the doctors."
            },
            {
                "role": "user",
                "content": dados_str
            },
        ],
        temperature=0.7,
        max_tokens=1000,
        top_p=1
    )
    
    # extrair a resposta do chatbot
    resposta = response.choices[0].message.content
    
    # adicionar a resposta como uma nova coluna no DataFrame
    dados['Comments'] = resposta
    
    # salvar o DataFrame modificado de volta em um arquivo CSV
    dados.to_csv(dados_path, index=False)
    
    return dados

dados_path = './dados.csv'
resultado = analyze_data(dados_path)
print(resultado)
