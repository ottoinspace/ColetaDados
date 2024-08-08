import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# # Exibir o texto
# print(extracao.text.strip())

numero_titulo = 0
numero_paragrafo = 0

# Filtrar a exibicao de tag
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('Titulo: \n', titulo)
        numero_titulo += 1
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)
        numero_paragrafo += 1

print('Total de titulos:', numero_titulo)
print('Total de paragrafos:', numero_paragrafo)
