from urllib.request import urlopen
from bs4 import BeautifulSoup
from Funcoes_JSON import carregar_contatos, guardar_contatos
import unidecode
import random


selecao = [
    'http://sexo=feminino&',
    'http://sexo=masculino&',
]
urls = random.choice(selecao)

url = urlopen(urls)
bsObj = BeautifulSoup(url.read(), "html.parser")

new = []
p = bsObj.find_all('input')
for d in p:
    new.append(d.get('value'))

# tira os acentos
dados = []
for x in new:
    dados.append(unidecode.unidecode(x))

contatos = carregar_contatos()

Nome = dados[5]
CPF = dados[6]
RG = dados[7]
Data_Nasci = dados[8]

CEP = dados[11]
Endereco = dados[12]
Numero = dados[13]
Bairro = dados[14]
Cidade = dados[15]
Estado = dados[16]

Fixo = dados[17]
Celular = dados[18]
mail = dados[9]

contatos[Nome] = {
    "nome": Nome,
    "cpf": CPF,
    "rg": RG,
    "data": Data_Nasci,
    "cep": CEP,
    "endereco": Endereco,
    "numero": Numero,
    "bairro": Bairro,
    "cidade": Cidade,
    "estado": Estado,
    "fixo": Fixo,
    "celular": Celular,
    "mail": mail,
}

guardar_contatos(contatos)
