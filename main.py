import requests
import json

vlr_inicial = int(input('Digite um valor inicial: '))
vlr_final = int(input('Digite um valor final: '))
codemp = input('Digite o código da Empresa: ')

url = ""
url_save = ""
url_get = ""


payload = {}
headers = {
    'Appkey': '',
    'Token': '',
    'Username': '',
    'Password': ''
}

response = requests.request("POST", url + '', headers=headers, data=payload)

bearerToken = response.json().get('bearerToken')
print("bearer ", bearerToken)


def post_request(payload):
    headers_save = {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer '+ bearerToken
    }
    
    headers.update(headers_save)

    response = requests.request("POST", url + url_save, headers=headers, data=payload)
    return print(response.text)

def get_ramais():
    headers_save = {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer '+ bearerToken
    }
    headers.update(headers_save)
    
    payload = json.dumps({ })

    response = requests.request("POST", url + url_get, headers=headers, data=payload)

    ramais = response.json().get('').get('result')
    print(ramais)
    create_payload(ramais)


def verify_ramal(vlr_atual, ramais):
    qtd_equal = 0
    for ramal in ramais:
        ramal = ramal[0]
        ramal = int(ramal)
        if (vlr_atual == ramal):
            qtd_equal += 1 
    if (qtd_equal == 0):
        return(True)
    else:
        return(False)

def create_payload(ramais):
    vlr_atual = 0
    for i in range(vlr_inicial -1, vlr_final):

        if (vlr_atual == 0):
            vlr_atual = vlr_inicial
        else:
            vlr_atual += 1
        verified = verify_ramal(vlr_atual, ramais)

        if (verified == True):
            payload = json.dumps({ })
            post_request(payload)      
                

get_ramais()
