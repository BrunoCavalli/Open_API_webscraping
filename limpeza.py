""" Modulo de preparacao e limpeza de dados """

import re

# este pequeno modulo ira limpar os dados

def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

# essa função ira manter apenas os caracteres numericos da string

def arruma_negocio(str):
    palavra = "opiniões"
    return str.replace(palavra, f" {palavra}")

# essa função ira criar um espaço na frente da palavra 'opiniao'
