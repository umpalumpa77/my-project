"""Программа  для обращения к API GitHub"""

import requests

response = requests.get("https://api.gitgub.com")
print(response.json())