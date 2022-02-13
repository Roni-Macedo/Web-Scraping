
import os
import json


"""   funçoes para salvar o resultado do scraping em json  """


def carregar_contatos():
    contatos = {}

    if os.path.exists('dados.json'):
        with open('dados.json', 'r') as f:
            contatos = json.load(f)

    return contatos


def guardar_contatos(contatos):
    with open('dados.json', 'w') as f:
        json.dump(contatos, f, indent=4)
