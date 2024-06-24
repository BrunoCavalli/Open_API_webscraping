import requests
import pandas as pd
from bs4 import BeautifulSoup
import doctoralia

urls = doctoralia.dados['Link']

review = {
    'Doutor': [],
    'Nome': [],
    'Estrelas': [],
    'Avaliacao': [],
    'Data': []
}

for url in urls:
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    doutor = soup.find('span', {'itemprop': 'name'}).text.strip()
    
    limite = 0

    for comentario in soup.find_all('div', {'class': 'media opinion text-break'}):
    
        review['Doutor'].append(doutor)
    
        nome = comentario.find('span', {'itemprop': 'name'}).text.strip()
        review['Nome'].append(nome)
    
        estrelas = comentario.find('div', {'id': 'rating-as-stars'})
        estrelas = estrelas.find('div').get('data-score')
        review['Estrelas'].append(estrelas)
    
        avaliacao = comentario.find('p', {'class': 'text-break'}).text.strip()
        review['Avaliacao'].append(avaliacao)
    
        data = comentario.find('time').text
        review['Data'].append(data)

        limite += 1
        if limite > 10:
            break
        
df = pd.DataFrame(review)

print(df)

df.to_csv('./review.csv', index=False)