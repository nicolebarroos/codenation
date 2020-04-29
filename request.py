import requests
import json
#
def postar():
    urlpost = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=df296d7c7f81cf5003892f24df518839ccf91708'
    file = {"answer": open("answer.json", "rb")}
    r = requests.post(urlpost, files=file)
    

    print(r.status_code)

if __name__ == '__main__':
    
    postar()