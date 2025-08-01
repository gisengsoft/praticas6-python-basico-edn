# 🧪 Atividade Prática 06 — Consumo de APIs e Geração Aleatória

Este repositório contém os códigos desenvolvidos como parte da **Prática 06** da formação **Escola da Nuvem (EDN)**.  
O objetivo é exercitar o uso de bibliotecas como `random` e o consumo de APIs externas via `requests`.

---

## 📂 Estrutura das Atividades

Cada pasta contém um programa em Python que resolve um problema específico:

### 1️⃣ senha_aleatoria/
Gera uma **senha aleatória personalizada**, com a quantidade de caracteres definida pelo usuário.

- Utiliza: `random`, `string`
- Entrada: quantidade de caracteres
- Saída: senha gerada

---

### 2️⃣ usuario_aleatorio/
Gera e exibe um **perfil de usuário aleatório** a partir da API [Random User Generator](https://randomuser.me).

- Utiliza: `requests`
- Dados exibidos: nome completo, e-mail e país.

---

### 3️⃣ consulta_cep/
Consulta dados de **endereço via CEP** utilizando a [API ViaCEP](https://viacep.com.br/).

- Entrada: CEP
- Saída: logradouro, bairro, cidade e UF.

---

### 4️⃣ cotacao_moeda/
Consulta a **cotação de moedas estrangeiras em relação ao Real (BRL)** utilizando a [API AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).

- Entrada: código da moeda (ex: `USD`, `EUR`, `GBP`)
- Saída: valor atual, máximo, mínimo, data e hora da última atualização.

---

## ▶️ Como Executar

Você pode executar cada script individualmente via terminal:

```bash
python nome_do_arquivo.py
```

---

## 📦 Requisitos

- Python 3.8 ou superior
- Biblioteca externa:
  - `requests` (instale com `pip install requests`)

---

## ✍️ Autor

**Gilson Inacio**  
🔗 [LinkedIn](https://www.linkedin.com/in/gilsoninsilva/)  
🔗 [GitHub](https://github.com/gisengsoft)
