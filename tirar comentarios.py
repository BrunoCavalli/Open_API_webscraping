""" Modulo para tirar os comentarios """

from openAPI import analyze_data

dados_path2 = './review.csv'

# perguntas da tabela review
perguntas_review = [
    "O comentário é positivo ou negativo?",
    "Qual é a média inteira das estrelas do doutor?"
]

resultado = analyze_data(dados_path2, perguntas_review)
print(resultado)
