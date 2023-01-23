import json
import lxml.html
import requests

'''
  'email': 'xalax48121@xegge.com',
  'password': 'KivAknZcs5yep'
'''

base_url = 'https://petfriends.skillfactory.ru'
endpoint = 'api/key'
url = f'{base_url}/{endpoint}'

headers = {
  'email': '', #'xalax48121@xegge.com'
  'password': '', #'KivAknZcs5yep'
}

result = {
  'status': 0,
  'content': {},
  'message': ''
}

r = requests.get(url, headers=headers)

result['status'] = r.status_code
content_type = r.headers.get('content-type')
if 'text/html' in content_type:
    tree = lxml.html.fromstring(r.text)
    header = tree.xpath('//h1/text()')[0]
    text = tree.xpath('//p/text()')[0]
    result['message'] = f'{header}. {text}'

elif 'application/json' in content_type:
    result['content'] = r.json()
else:
    raise Exception(f'Unknown content-type: {content_type}')




'''text/html; charset=utf-8'''
'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>This user wasn&#x27;t found in database</p>'''

'''application/json'''
'''{"key":"1d6f479dbf5d120610954f4dfd4bb17b090b57aa38ea73c5ff92c37d"}'''