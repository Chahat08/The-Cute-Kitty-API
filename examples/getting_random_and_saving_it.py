from urllib.request import urlopen, urlretrieve
import json

resp = urlopen(r'https://cutekitty.pythonanywhere.com/catto/random').read()
data = json.loads(resp)

print(data)
urlretrieve(data['img'], str(data['name'])+data['img'][-4:])