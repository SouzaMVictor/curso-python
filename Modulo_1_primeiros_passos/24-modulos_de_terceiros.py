# pacotes ou bibliotecas que não fazem parte do padrão python
# criados por terceiros
# instalados pelo pip

print("importação e uso de módulo de terceiros")

import requests
# biblioteca para requisições http

url ="https://www.exemple.com"
response = requests.get(url)
print(f"solicitação http para {url} retornou o status {response.status_code}")


# encontrar bibliotecas de terceiros
# https://pypi.org/