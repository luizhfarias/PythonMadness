import requests
cep = input('Informe o CEP: ')

response = requests.get('https://viacep.com.br/ws/'+cep+'/json/', auth=('', ''))

data = response.json()

print(data['logradouro'])
print(data['localidade'])

print(data)