'''____________________Módulo Principal____________________'''

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.doctoralia.com.br/pesquisa?q=Psiquiatra&loc=Rio%20de%20Janeiro&filters%5Bspecializations%5D%5B%5D=78"
page =  requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')

dados = {
    'Nome': [],
    'Profissão': [],
    'Valor da Consulta': [],
    'Endereço': [],
    'Tem Teleconsulta?': [],
    'Número de Opiniões': [],
    'Tem Perfil Verificado?': [],
    'Assinatura': [],
    'Tem Fidelidade dos Pacientes?': [],
    'Currículo': [],
    'Comentários': []
}

for doctoralia in soup.find_all('div', {'class': 'card card-shadow-1 mb-1'}):

    nome = doctoralia.find('span', {'itemprop': 'name'}).text
    dados['Nome'].append(nome)

    profissao = doctoralia.find('span', {'data-test-id': 'doctor-specializations'}).text
    dados['Profissão'].append(profissao)

    valor = doctoralia.find('span', {'itemprop': 'name'}).text
    dados['Valor da Consulta'].append(valor)

    endereco = doctoralia.find('span', {'class': 'text-truncate'}).text
    dados['Endereço'].append(endereco)

    teleconsulta = doctoralia.find('span', {'itemprop': 'name'}).text
    dados['Tem Teleconsulta?'].append(teleconsulta)

    opiniao = doctoralia.find('a', {'data-ga-label': 'Reviews'}).text

    def ajeita_negocio(str):
        return re.sub(r'[^0-9]', '', str)

    opiniao = ajeita_negocio(opiniao)
    dados['Número de Opiniões'].append(opiniao)

    perfil_verificado = doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    dados['Tem Perfil Verificado?'].append(perfil_verificado)

    assinatura =  doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    dados['Assinatura'].append(assinatura)

    fidelidade =  doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    dados['Tem Fidelidade dos Pacientes?'].append(fidelidade)

    curriculo =  doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    dados['Currículo'].append(curriculo)

    comentarios =  doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    dados['Comentários'].append(comentarios)


df = pd.DataFrame(dados)

print(df)

df.to_csv('./dados.csv', index=False)
