import requests

# Consulta a API Random User Generator
url = "https://randomuser.me/api/"
resposta = requests.get(url)
dados = resposta.json()

# Extrai e exibe informações
usuario = dados["results"][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario['email']
pais = usuario['location']['country']

print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
