import json
from base64 import b64decode


def get_auth_data(token: str) -> str:
  base64_bytes = token.encode()
  result = b64decode(base64_bytes)
  data = json.loads(result.decode())
  return data.get('email'), data.get('password')
