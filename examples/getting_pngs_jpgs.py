from urllib.request import urlopen, urlretrieve
import json

resp = urlopen(r'https://cutekitty.pythonanywhere.com/catto/search/?type=jpg&type=png').read()
data = json.loads(resp)

print(data)