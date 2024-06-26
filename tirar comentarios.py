""" Modulo para tirar os comentarios """

from openAPI import analyze_data

dados_path2 = './review.csv'

# perguntas da tabela review
perguntas_review = [
    "O comentário é positivo ou negativo?"
]

resultado = analyze_data(dados_path2, perguntas_review)
print(resultado)
