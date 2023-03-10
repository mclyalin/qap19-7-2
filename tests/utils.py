import json
from base64 import b64decode

import lxml.html


def get_auth_data(token: str) -> str:
    base64_bytes = token.encode()
    result = b64decode(base64_bytes)
    data = json.loads(result.decode())
    email = data.get('email')
    password = data.get('password')
    return email, password


def parse(response):
    status = response.status_code
    data = {}
    message = ''

    content_type = response.headers.get('content-type')
    if 'text/html' in content_type:
        tree = lxml.html.fromstring(response.text)
        header = tree.xpath('//h1/text()')[0]
        text = tree.xpath('//p/text()')[0]
        message = f'{header}. {text}'
    elif 'application/json' in content_type:
        data = response.json()
    else:
        raise Exception(f'Unknown content-type: {content_type}')

    return status, data, message