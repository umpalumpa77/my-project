import requests
import pprint
import json
from prettytable import PrettyTable

def get_random_user_data(num_users=5):
    url = f"https://randomuser.me/api/?results={num_users}"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ошибка при запросе: {e}")
        return None


def extract_user_info(data):
    user_info = []

    for user in data[results]:
        name = f"{user['name']['first']} {user['name']['last']}"
        gender = f"{user['gender']}"
        email = f"{user['email']}"
        country = f"{user['location']['country']}"
        age = f"{user['dob']['age']}"
        user_info.append((name, gender, age, email, country))

    return user_info

def print_user_info_table(user_info):
    table = PrettyTable()
    table.field_names = ["Имя", "Пол", "Возраст", "Email", "Страна"]

    for info in user_info:
        table.add_row(info)
        
    return table

def main():
    num_users = int(input("Введите кол-во пользовталей для получения"))
    data = get_random_user_data(num_users=num_users)

    if data:
        print(f"\nПолучены данные о {num_users} пользователях: ")
        user_info = extract_user_info(data)
        print_user_info_table(user_info=user_info)
    else:
        print("не удалось получить данные о API")

if __name__ == "__main__":
    main()
