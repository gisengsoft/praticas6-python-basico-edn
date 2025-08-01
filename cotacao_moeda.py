import requests

moeda = input("Código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
resposta = requests.get(url)
dados = resposta.json()

chave = moeda + "BRL"
if chave in dados:
    info = dados[chave]
    print(f"Moeda: {info['name']}")
    print(f"Valor Atual: R$ {info['bid']}")
    print(f"Valor Máximo: R$ {info['high']}")
    print(f"Valor Mínimo: R$ {info['low']}")
    print(f"Data: {info['create_date']}")
else:
    print("Moeda inválida ou não encontrada.")
