from openAPI import analyze_data

dados_path2 = './review.csv'
perguntas_review = [
    "O comentário é positivo ou negativo?"
]

resultado = analyze_data(dados_path2, perguntas_review)
print(resultado)