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

def receber_arquivo(file_url)

enviar_arquivo()
