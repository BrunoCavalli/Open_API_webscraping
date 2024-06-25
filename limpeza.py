""" Modulo de preparacao e limpeza de dados """

import re
def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

# Este pequeno módulo limpa os dados 
