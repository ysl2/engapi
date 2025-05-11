import requests
import json
import config

headers = {
   'User-Agent': 'Mozilla/5.0',
   'Authorization': f'NIS {config.FRDIC_API_KEY}',
}
url = "https://api.frdic.com/api/open/v1/studylist/category?language=en"
res = requests.get(url, headers=headers)
res = json.loads(res.text)
res = res['data']
res = [item for item in res if item['name'] == config.FRDIC_LIBNAME]
res = res[0]['id']

url = f'https://api.frdic.com/api/open/v1/studylist/words/{res}?language=en'
res = requests.get(url, headers=headers)
res = json.loads(res.text)
res = res['data']
frdic = [item['word'] for item in res]

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {config.MAIMEMO_API_KEY}',
}
url = 'https://open.maimemo.com/open/api/v1/notepads'
res = requests.get(url, headers=headers)
res = json.loads(res.text)
res = res['data']['notepads']
res = [item for item in res if item['title'] == config.MAIMEMO_LIBNAME]
id = res[0]['id']

url = f'https://open.maimemo.com/open/api/v1/notepads/{id}'
res = requests.get(url, headers=headers)
res = json.loads(res.text)
res = res['data']['notepad']
res['content'] = res['content'].split('\n')
res['content'] = [item for item in res['content'] if item]
res['content'] = res['content'][1:]
res['content'] = res['content'] + frdic
res['content'] = list(dict.fromkeys(res['content']))
res['content'] = [f"#{res['title']}"] + res['content']
res['content'] = '\n'.join(res['content'])
print(res['content'])

url = f'https://open.maimemo.com/open/api/v1/notepads/{id}'
res = requests.post(url, headers=headers, json={'notepad': res})
print(res.text)
