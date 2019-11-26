import requests


def main():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NjI5OTM4LCJqdGkiOiJiNTc1NT' \
          'cxZDM3M2M0YTQxOTNiNzJmZDBlODI3OWNiNiIsInVzZXJfaWQiOjF9.gfwkS7OUAconQavq81EU-doLMh9ka7BiVRYkiKi0irc'
    key_refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDcxNDU1OSwianRpI" \
                  "joiY2EwYmEzY2VjNWRlNDQwZGI3ZmI0YzBjNGEzMzJkNTYiLCJ1c2VyX2lkIjoxfQ.fUyTPJMhiFzOHyNLUe82RMmm-fSNv" \
                  "scS9N4enSG4yuE"
    # consulta()
    # refresh_key(key_refresh)
    # get_key("brendon", "123456789")
    get_key_2()
    print()


def consulta(key=""):
    urlget = 'http://127.0.0.1:8000/clientes/'
    urlget = 'http://127.0.0.1:8000/lojas2/'

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
    print("Key de atualização: ", r.json()['refresh'])


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
