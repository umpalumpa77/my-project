# import requests
# import json
# import pprint

# response = requests.get("https://randomuser.me/api")
# if response.ok:
#     data = response.json()
#     user = data["results"][0]
#     print(f"имя: {user['name']['first']}")
#     print(f"Страна: {user['location']['country']}")
#     print("-"* 30)
#     print("printing data")
#     pprint.pprint(data)
#     print("Printing user")
#     pprint.pprint(user)
# else:
#     print("Ошибка получения данных")

import requests 

response = requests.get("htpps://apo.quotable.io/random")

if response.status_code == 200:
    data = response.json()
    print(f"Случайная цитата: '{data['content']}' - {data['author']}")
else:
    print("Не удалось получить цитату")