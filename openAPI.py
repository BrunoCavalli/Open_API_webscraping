""" Modulo de implementação da analise dos dados com API da openai """

import DoctorAlia
import pandas as pd
from openai import OpenAI
client = OpenAI(api_key="API-KEY")




dados = pd.read_csv('./dados.csv')
#print(dados)
dados_str = dados.to_string()



response = client.chat.completions.create(
 model="gpt-3.5-turbo",
 messages=[
   {
     "role": "assistant",
     "content": "You will be provided with an csv file, and your task is to make comentaries of it."
   },
   {
        "role": "user",
        "content": dados_str
   },
 ],
 temperature=0.7,
 max_tokens=1000,
 top_p=1
)


resposta = response.choices[0].message.content
print(resposta)
