from urllib.request import urlopen, urlretrieve
import json

resp = urlopen(r'http://127.0.0.1:8000/catto/random/').read()
data = json.loads(resp)

print(data)
urlretrieve(data['img'], data['name']+data['img'][-4:])