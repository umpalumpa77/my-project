import requests
import json

response = requests.get("https://randomuser.me/api")
if response. ok:
    data = response.json()
    user = data["results"][0]
    print(f"имя: {user['name']['first']}")
    print(f"Страна: {user['location']['country']}")
    print("-"* 30)
    print("printing data")
    pprint.pprint(data)
    print("Printing user")
    pprint.pprint(user)
else:
    print("Ошибка получения данных")
