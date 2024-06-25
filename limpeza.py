""" Modulo de preparacao e limpeza de dados """

import re
def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

def arruma_negocio(str):
    return (str).ljust(10)

# Este pequeno módulo limpa os dados 
