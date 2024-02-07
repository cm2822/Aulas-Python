import requests

def verificar(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"O site {url} está acessível.")

        else:
            print(f"O site {url} não está acessível. Código de resposta --> {response.status_code}")
    except requests.ConnectionError:
        print(f"Não foi possível conectar com o site devido a {url}. Verifique a sua Internet.")


url = "https://www.iefp.pt"

verificar(url)
