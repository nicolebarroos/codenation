#Codenation Criptografia
import requests
import hashlib
import json

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
tk = "df296d7c7f81cf5003892f24df518839ccf91708"

urlgit = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={0}'.format(tk)
response = requests.get(urlgit)
response_json = response.json()
numero_casas = response_json['numero_casas']
cifrado = response_json['cifrado']
token = response_json['token']

def decifrar():
    msg = ''
    for x in cifrado:
        if x in alfabeto:
            pos = alfabeto.index(x)
            msg += alfabeto[pos - numero_casas]
        else:
            msg += x
    return msg.lower()

orig = decifrar()
resumo = hashlib.sha1(str(orig).encode('utf-8')).hexdigest()

resultado = {
"numero_casas": numero_casas,
"token": token,
"cifrado": cifrado,
"decifrado": orig,
"resumo_criptografico": resumo
}

   
if __name__ == '__main__':
    print(resultado)
    #criar_arquivo()
    