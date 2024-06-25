import pandas as pd
from openai import OpenAI
import concurrent.futures

# Inicializar o cliente OpenAI com a chave da API
chave_api = input("digite sua chave aqui:")
client = OpenAI(api_key=chave_api)

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1
    )
    return response.choices[0].message.content
    
def process_row(row, pergunta):
    prompt = [
        {"role": "assistant", "content": "You will receive a CSV row, your task is to make comments about the content of it."},
        {"role": "user", "content": row.to_string()},
        {"role": "user", "content": pergunta}
    ]
    return get_response(prompt)

def analyze_data(dados_path, perguntas):
    # Ler o arquivo CSV
    dados = pd.read_csv(dados_path)
    
    # Iterar sobre a lista de perguntas
    for idx, pergunta in enumerate(perguntas):
        coluna_nome = f'{pergunta}'
        dados[coluna_nome] = ""
        
        # Using ThreadPoolExecutor for parallel API calls
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(process_row, dados.iloc[i], pergunta): i for i in range(len(dados))}
            for future in concurrent.futures.as_completed(futures):
                idl = futures[future]
                resposta = future.result()
                dados.at[idl, coluna_nome] = resposta
    
    # Salvar o DataFrame modificado de volta em um arquivo CSV
    dados.to_csv(dados_path, index=False)
    
    return dados

def analyze_review(dados_path, perguntas):
    # Ler o arquivo CSV
    review = pd.read_csv(dados_path)
    
    # Iterar sobre a lista de perguntas
    for idx, pergunta in enumerate(perguntas):
        coluna_nome = f'{pergunta}'
        review[coluna_nome] = ""
        
        # Using ThreadPoolExecutor for parallel API calls
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(process_row, review.iloc[i], pergunta): i for i in range(len(review))}
            for future in concurrent.futures.as_completed(futures):
                idl = futures[future]
                resposta = future.result()
                review.at[idl, coluna_nome] = resposta
    
    # Salvar o DataFrame modificado de volta em um arquivo CSV
    review.to_csv(dados_path, index=False)
    
    return review
