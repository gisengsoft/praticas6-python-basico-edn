import random
import string

# Solicita quantidade de caracteres
qtd = int(input("Quantidade de caracteres para a senha: "))

# Define o conjunto de caracteres possíveis
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(qtd))
print(f"Senha gerada: {senha}")
