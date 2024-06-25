""" Modulo de preparacao e limpeza de dados """

import re

# este pequeno módulo irá limpar os dados

def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

# essa função irá manter apenas os caracteres númericos da string

def arruma_negocio(str):
    palavra = "opiniões"
    return str.replace(palavra, f" {palavra}")

# essa função irá criar um espaço na frente da palavra 'opiniao'
