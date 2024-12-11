import requests

def get_guess_by_name():

    name = input("Введите имя для проверки ")
    params = {"name": name}
    
    response_gender = requests.get(url=URL_GENDER, params=params )
    response_age = requests.get(url=URL_AGE, params=params )
    response_nationality = requests.get(url=URL_NATIONALITY, params=params)

    resp_json_gender = response_gender.json()
    resp_json_age = response_age.json()
    resp_json_nationality = response_nationality.json()

    print(f"Вы ввели имя - {name} ")
    print(f"{name} является {resp_json_gender['gender']} с вероятностью {resp_json_gender['probability']}")
    print(f"{name} примерно {resp_json_age['age']}")
    print(f"{name} может быть из \n")
    for i in resp_json_nationality['country']:
        print(f"{i["country_id"]} с вероятностью {i["probability"]}")

    # print("данные по полу")
    # print(resp_json_gender)
    # print("данные по возрасту")
    # print(resp_json_age)
    # print("данные по национальности")
    # print(resp_json_nationality)

URL_GENDER =  "https://api.genderize.io"
URL_AGE =   "https://api.agify.io"
URL_NATIONALITY ="https://api.nationalize.io"



get_guess_by_name()