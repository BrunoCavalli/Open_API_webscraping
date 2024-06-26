""" Modulo para tirar os dados """

from openAPI import analyze_data

dados_path1 = './dados.csv'

# perguntas da tabela dados
perguntas_dados = [
    "Em uma palavra, qual é o bairro desse endereco?",
    "O valor da consulta é considerada caro ou barato, considerando a média de 350 reais?"
]

resultado = analyze_data(dados_path1, perguntas_dados)
print(resultado)
