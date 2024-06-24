import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from limpeza import ajeita_negocio

url = "https://www.doctoralia.com.br/pesquisa?q=Psiquiatra&loc=Rio%20de%20Janeiro&filters%5Bspecializations%5D%5B%5D=78"
page =  requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')

dados = {
    'Nome': [],
    'Especialidade': [],
    'Valor da Consulta': [],
    'Endereco': [],
    'Numero de Opinioes': [],
    'Tem Perfil Verificado?': [],
    'Tem Fidelidade dos Pacientes?': [],
    'Assinatura': [],
    'Link' : []
}

for doctoralia in soup.find_all('div', {'class': 'card card-shadow-1 mb-1'}):
    
    nome = doctoralia.find('span', {'itemprop': 'name'}).text.strip()
    dados['Nome'].append(nome)

    especialidade = doctoralia.find('span', {'data-test-id': 'doctor-specializations'}).text.strip()
    dados['Especialidade'].append(especialidade)
    
    valor = doctoralia.find('p', {'class': 'm-0 text-nowrap font-weight-bold'})
    if valor is not None:
       valor = str(valor.get_text())
       valor = ajeita_negocio(valor)
    else:
       valor = None
    if valor == "0" or valor is None or valor.strip() == "":
       valor = "Não definido"
    else:
       valor = "R$ " + valor
    dados['Valor da Consulta'].append(valor)    
    
    endereco = doctoralia.find('span', {'class': 'text-truncate'}).text
    dados['Endereco'].append(endereco)
    
    opiniao = doctoralia.find('a', {'data-ga-label': 'Reviews'}).text
    opiniao = ajeita_negocio(opiniao)
    dados['Numero de Opinioes'].append(opiniao)
    
    perfil_verificado = []
    selo_1 = doctoralia.find('i', {'class': 'svg-icon svg-icon-check-filled svg-icon-size-12 svg-icon-color-secondary'})
    
    if selo_1:
        perfil_verificado.append("Sim")
    else:
        perfil_verificado.append("Nao")
    
    perfil_verificado = perfil_verificado[0]
    dados['Tem Perfil Verificado?'].append(perfil_verificado)
    
    fidelidade =  []
    selo_2 = doctoralia.find('i', {'class': 'svg-icon svg-icon-trust svg-icon-size-18 svg-icon-color-secondary mr-1'})
    
    if selo_2:
        fidelidade.append("Sim")
    else:
        fidelidade.append("Nao")
    
    fidelidade = fidelidade[0]
    dados['Tem Fidelidade dos Pacientes?'].append(fidelidade)
    
    assinatura = []
    novo = doctoralia.find('span', {'class': 'badge bg-success-light'})
    premium = doctoralia.find('div', {'data-test-id': 'first-class-badge'})
    
    if novo:
        assinatura.append("Perfil novo")
    elif premium:
        assinatura.append("First Class")
    else:
        assinatura.append("Nao tem assinatura")

    assinatura = assinatura[0]
    dados['Assinatura'].append(assinatura)
    
    link = doctoralia.find('a', {'data-id': 'address-context-cta'})
    link = link.get('href')
    dados['Link'].append(link)

df = pd.DataFrame(dados)

print(df)

df.to_csv('./dados.csv', index=False)
