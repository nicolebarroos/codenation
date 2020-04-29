import requests


r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=df296d7c7f81cf5003892f24df518839ccf91708')
r.json()
print(r.json())
