import requests


def main():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc1MTc2OTE1LCJqdGkiOiJjODk4ZmE3YTBjMDk0ZmQyYjg5NTc5NTQ0ZjIyYTg0YSIsInVzZXJfaWQiOjEwfQ.hrY6vQjb8d2oB2IsEqZm_GgkXT1uRgCGCV-oHxVNItw'
    key_refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NTI2MTQxNSwianRpIjoiM2NiZmI3OWRkZTdiNDc0MDkwYWI0MmIyZmQxZTA2ZDIiLCJ1c2VyX2lkIjoxMH0.uG5K_GFj0K5kb7Ru6VSO2DVxGp_cnLpIevOJS2rxWN4"
    # refresh_key(key_refresh)

    # get_key("brendon", "123456789")
    consulta(key)
    # consulta2()
    print()


def consulta(key=""):
    urlget = 'http://127.0.0.1:8000/clientes/'

    if key != "":
        headers = {
            "Authorization": "Bearer " + key}
        r = requests.get(urlget, headers=headers)
    else:
        r = requests.get(urlget)
    print(r.json())


def consulta2(key=""):
    urlget = 'http://127.0.0.1:8000/lojas/'

    if key != "":
        headers = {
            "Authorization": "Bearer " + key}
        r = requests.get(urlget, headers=headers)
    else:
        r = requests.get(urlget)
    print(r.json())

def get_key(username, password):
    url_key_get = 'http://127.0.0.1:8000/api/token/'
    body = {
        "username": username,
        "password": password
    }
    r = requests.post(url_key_get, json=body)
    if r.status_code == 200:
        print("Key de acesso: ", r.json()['access'])
        print("Key de atualizacao: ", r.json()['refresh'])
    else:
        print(r.json())
        print('erro')

def refresh_key(key):
    url_key_refresh = 'http://127.0.0.1:8000/api/token/refresh/'
    body = {
        "refresh": key
    }

    r = requests.post(url_key_refresh, json=body)
    print(r.json())





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
