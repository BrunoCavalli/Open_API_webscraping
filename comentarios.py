""" Modulo dos comentarios """

import requests
import pandas as pd
from bs4 import BeautifulSoup
import doctoralia

# importar a coluna do modulo principal com os links dos perfis dos medicos
urls = doctoralia.dados['Link']

# criar dicionario com os cabecalhos das colunas da extracao de dados dos comentarios
review = {
    'Doutor': [],
    'Nome': [],
    'Estrelas': [],
    'Avaliacao': [],
    'Data': []
}

# iniciar loop para analisar um perfil por vez
for url in urls:
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

# extrair nome do medico da url sem expaços
    doutor = soup.find('span', {'itemprop': 'name'}).text.strip()

# iniciar contador de comentarios da pagina
    limite = 0

# iniciar loop para inspecionar cada caixa de comentario
    for comentario in soup.find_all('div', {'class': 'media opinion text-break'}):

# adicionar nome do doutor a coluna
        review['Doutor'].append(doutor)
    
# adicionar nome da pessoa que fez o comentário
        nome = comentario.find('span', {'itemprop': 'name'}).text.strip()
        review['Nome'].append(nome)
    
# adicionar número de estrelas
        estrelas = comentario.find('div', {'id': 'rating-as-stars'})
        estrelas = estrelas.find('div').get('data-score')
        review['Estrelas'].append(estrelas)
    
# extrair comentario escrito 
        avaliacao = comentario.find('p', {'class': 'text-break'}).text.strip()
        review['Avaliacao'].append(avaliacao)
    
# extrair data do comentario
        data = comentario.find('time').text
        review['Data'].append(data)

# aumenta a contagem e finaliza a iteração quando esta chegar a 10
        limite += 1
        if limite > 10:
            break
        
# cria DataFrame      
df = pd.DataFrame(review)
print(df)

# transforma o DataFrame em um arquivo csv
df.to_csv('./review.csv', index=False)
