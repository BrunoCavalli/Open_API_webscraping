""" Modulo de preparacao e limpeza de dados """

import re

def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

def arruma_negocio(str):
    palavra = "opiniões"
    return str.replace(palavra, f" {palavra}")

# este pequeno módulo irá limpar os dados 
