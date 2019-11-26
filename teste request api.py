import requests


def main():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0Nzc4NTc5LCJqdGkiOiJhZDZhOWZiMDk4ZjI0ZDNmOWM0NTVjNzQ1NmRhYjE0ZiIsInVzZXJfaWQiOjF9.yxbXYqYJV-pYtwRZKQf4ZrCQ2OlTaTozOnGPHMGhZ3c'
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0Nzc4NjgzLCJqdGkiOiJjZjhiMGRiYWM4MDA0OGQyYWIyNWVkZDFiOTQ5ZjAyMCIsInVzZXJfaWQiOjN9.eGRbasu8NC29oT89FoYjr0L08WSBIsPBaX4MPK-yE3Y'
    key_refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDg2NDA2NSwianRpIjoiYjA5NWNiNzRlZTNjNDkzMWFiY2QyM2FjYTc2NGQ5YTkiLCJ1c2VyX2lkIjoxfQ.IFS8JjMHmJWXbUOU_MxA53N9lSxtaTwo2pPIl-6kjks"
    key_refresh = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDg2NDc4MywianRpIjoiOTA5OGExNjYzYzQwNDE3ZTk0Zjc4YjgyM2QxY2EyYmMiLCJ1c2VyX2lkIjozfQ.fOrjCToktN7bjkTDxOERRoFFh-4bSHcs0K9HLT3-6Q4'
    consulta(key)
    # refresh_key(key_refresh)
    # get_key("Lucas", "123456789")

    print()


def consulta(key=""):
    urlget = 'http://127.0.0.1:8000/clientes/'
    urlget = 'http://127.0.0.1:8000/lojas/2/'

    if key != "":
        headers = {
            "Authorization": "Bearer " + key}
        r = requests.get(urlget, headers=headers)
    else:
        r = requests.get(urlget)
    print(r.json())


def refresh_key(key):
    url_key_refresh = 'http://127.0.0.1:8000/api/token/refresh/'
    body = {
        "refresh": key
    }

    r = requests.post(url_key_refresh, json=body)
    print(r.json())


def get_key(username, password):
    url_key_get = 'http://127.0.0.1:8000/api/token/'
    body = {
        "username": username,
        "password": password
    }
    r = requests.post(url_key_get, json=body)
    print("Key de acesso: ", r.json()['access'])
    print("Key de atualizacao: ", r.json()['refresh'])


def get_key_2():
    url = 'http://127.0.0.1:8000/o/token/'
    body = {
        "username": 'brendon',
        "password": '123456789'
    }

    r = requests.post(url, json=body)
    print(r.json())

if __name__ == '__main__':
    main()
