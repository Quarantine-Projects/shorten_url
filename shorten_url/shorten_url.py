import requests
import json

def url_short(url):
    response = requests.post('https://rel.ink/api/links/', data={"url": url})
    if response.status_code == 201:
        data = json.dumps(response.json())
        output = json.loads(data)
        output = 'https://rel.ink/' + str(output['hashid'])
    else:
        return response.status_code
    return output

def url_expand(url):
    response = requests.get('https://rel.ink/api/links/' + url.split('rel.ink/')[1])
    if response.status_code == 200:
        data = json.dumps(response.json())
        output = json.loads(data)
        output = str(output['url'])
    else:
        return response.status_code
    return output
