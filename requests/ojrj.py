# import requests

# URL = "https://official-joke-api.appspot.com/random_joke"

# response = requests.get(url=URL)

# print(f"Ответ response - {response}")
# print(f"Статус-код ответа - {response.status_code}")
# print(f"Текст ответа - {response.text}\n")
# resp_json = response.json()
# print(f"JSON ответа - {resp_json}\np")

# print(f"""
# Номер шутки: {resp_json['id']}
# Тип шутки {resp_json['type']}
# сетап : {resp_json['setup']}
# панчлайн: {resp_json['punchline']}
# """)

def get_types(url):
    response =  requests.get(url+"types")
    resp_json = response.json()
    print(resp_json)
    print("Выберите тип шутки")
    for i in range(len(resp_json)):
        print(f"{i}: {resp_json[i]}")
    ans = int(input("Введите цифру для типа шутки: "))
    return resp_json[ans]

def get_joke_by_type(url, type):
    response = requests.get(f"{url}jokes/{type}/random")
    resp_json = response.json()
    print(f"""
Сетап: {resp_json[0]['setup']}
Панчлайн: {resp_json[0]['punchline']}""")


import requests

URL = "https://official-joke-api.appspot.com/"

ans = ""
while ans != "-":
    type = get_types(URL)
    get_joke_by_type(URL, type)
    ans = input("нажми '-' чтобы выйти\n")

