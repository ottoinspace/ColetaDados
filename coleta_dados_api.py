import requests


def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = r"C:\Users\arnol_73uf3lj\Pictures\firefly-honkai-star-rail-1.jpg"

    # Enviar o arquivo
    requisicao = requests.post(
        'https://file.io',
        files={'file': open(caminho, 'rb')},
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Aquivo enviado. Link para acesso", url)


def receber_arquivo(file_url):
    # Receber o arquivo
    requisicao = requests.get(file_url)

    # Salvar o aquivo
    if requisicao.ok:
        with open('aquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo:", requisicao.json)


enviar_arquivo()

receber_arquivo('https://file.io/D5sm67z80hrI')
