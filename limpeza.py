import re
def ajeita_negocio(str):
    return re.sub(r'[^0-9]', '', str)

#este pequeno módulo limpa os dados 
