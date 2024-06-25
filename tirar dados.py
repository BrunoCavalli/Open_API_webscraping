from OpenAPI import analyze_data

dados_path1 = './dados.csv'
perguntas_dados = [
    "O endereço fica em que zona do Rio de Janeiro?",
    "O valor da consulta é considerada caro ou barato, considerando a média de 350 reais?"
]

resultado = analyze_data(dados_path1, perguntas_dados)
print(resultado)