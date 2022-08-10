import requests

url = 'http://127.0.0.1:3001/'

user_data = {
    "nome": "nome válido",
    "password": "senha válida",
    "email": "email_valido@email.com"
}

responde = requests.put(url=url, json=user_data)
