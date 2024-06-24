"""Modulo de implementação da analize dos dados com API da openai"""

import DoctorAlia
import pandas as pd
from openai import OpenAI
client = OpenAI(api_key="API KEY")

file = client.files.create(
  file=open("dados.csv", "rb"),
  purpose='assistants'
)

"""
dados = pd.read_csv('./dados.csv')
#print(dados)
dados_str = dados.to_string()
"""

assistant = client.beta.assistants.create(
  instructions="Your task is to make coments about the data in the csv file that you will receive",
  model="gpt-3.5-turbo",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

responce= assistant.instructions[0]
print(responce)

"""
response = client.chat.completions.create(
 model="gpt-3.5-turbo",
 messages=[
   {
     "role": "assistant",
     "content": "You will be provided with an csv file, and your task is to make an analyzes of it."
   },
   {
        "role": "user",
        "content": dados_str
   },
 ],
 temperature=0.7,
 max_tokens=64,
 top_p=1
)


resposta = response['choices'][0]['message']['content']
"""
