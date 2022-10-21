# The Cute Kitty API
> A RESTful API listening to your GET requests for pictures of cats!  

The Cute Kitty API is a RESTful API created via Django. Use it to get random pictures of cute cats. It boasts of powerful quering and filtering fueled via the Django ORM.  

## Endpoints

- [https://cutekitty.pythonanywhere.com](https://cutekitty.pythonanywhere.com) - For a list of all cats in the database!
- [https://cutekitty.pythonanywhere.com/catto/random](https://cutekitty.pythonanywhere.com/catto/random) - To get a randomly chosen cat from the database!
- [https://cutekitty.pythonanywhere.com/catto/41](https://cutekitty.pythonanywhere.com/catto/41) - You can also get a cat from its name. This will return cat 41!
- [https://cutekitty.pythonanywhere.com/catto/search/?tags=cute&type=jpg](https://cutekitty.pythonanywhere.com/catto/search/?tags=cute&type=jpg) - Filtering the database to get a list of cute .jpg cat images!

## Filtering

Some ways in which you can query and filter the cat database:

| Requirement | Endpoint |
| ------ | ------ |
| I want to get a certain cat picture named 42 | [https://cutekitty.pythonanywhere.com/catto/42](https://cutekitty.pythonanywhere.com/catto/42) |
| I want pictures of "chonky" cats only! | [https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky](https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky) |
| I want pictures of "chonky" and "grey" cats only! | [https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky&tags=grey](https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky&tags=grey) |
| I only want ".gif" cat images! | [https://cutekitty.pythonanywhere.com/catto/search/?type=gif](https://cutekitty.pythonanywhere.com/catto/search/?type=gif) |
| I only want ".png" or ".jpg" cat images! | [https://cutekitty.pythonanywhere.com/catto/search/?type=jpg&type=png](https://cutekitty.pythonanywhere.com/catto/search/?type=jpg&type=png) |
| I only want ".gif" images of "cute" cats! | [https://cutekitty.pythonanywhere.com/catto/search/?tags=cute&type=gif](https://cutekitty.pythonanywhere.com/catto/search/?tags=cute&type=gif) |
| I only want ".jpg" or ".png" images of "chonky" and "cute" cats! | [https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky&tags=cute&type=jpg&type=png](https://cutekitty.pythonanywhere.com/catto/search/?tags=chonky&tags=cute&type=jpg&type=png) |

## Returned Data
The cat image model is of the form:
```json
{
        "name": 339,
        "img": "https://cutekitty.pythonanywhere.com/media/cats/5466.gif",
        "tags": "cute"
}
```
 - **Fetching cat by name, fetching a random cat**: The data is returned as a single JSON object.
 - **Fetching list of all cats, fetching filtered results of search**: The data is returned as an array of matching JSON objects.

## Using your cat image
To use your cat images, listen to the endpoints using your favourite programming language and simply access the "img" attribute of the returned JSON response.

### Example
This is a simple example of the same in Python. Find more examples [here](https://github.com/Chahat08/The-Cute-Kitty-API/tree/master/examples).

```py
from urllib.request import urlopen, urlretrieve
import json

resp = urlopen(r'http://127.0.0.1:8000/catto/random/').read()
data = json.loads(resp)

print(data)
urlretrieve(data['img'], data['name']+data['img'][-4:])
```
