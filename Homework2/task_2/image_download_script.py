import random
import requests

token = 632616764568400
hero_id = random.randint(1, 700)


url = f'https://superheroapi.com/api/{token}/{hero_id}'

response = requests.get(url)

full_name = response.json()['biography']['full-name'].replace(' ', '_')
image_url = response.json()['image']['url']
graphic_format = image_url[image_url.rindex('.'):]

image_name = f'{full_name}{graphic_format}'

if not full_name:
    name = response.json()['name'].replace(' ', '_')
    image_name = f'{name}{graphic_format}'

r = requests.get(image_url)


with open(image_name, 'wb') as im:
    im.write(r.content)
    im.close()
