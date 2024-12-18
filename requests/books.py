import requests
import pprint
import json
from prettytable import PrettyTable

def get_random_book(QUERY="", NUM_RESULTS=5):
    url = f"https://www.googleapis.com/books/v1/volumes?q={QUERY}&maxResults={NUM_RESULTS}&langRestrict=ru"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ошибка при запросе: {e}")
        return None
    

def extract_user_info(data):
    user_info = []

    for user in data['items']:
        title = f"{user['volumeInfo']['title']} "
        authors = f"{user['volumeInfo']['authors']}"
        publishedDate = f"{user['volumeInfo']['publishedDate']}"
        description = f"{user['volumeInfo']['description']}"
        user_info.append((title, authors, publishedDate, description,))

    return user_info

def get_user_info_table(user_info):
    table = PrettyTable()
    table.field_names = ["Название", "Автор", "Дата", "Описание" ]

    for info in user_info:
        table.add_row(info)
        
    return table

def main():
    num_results = int(input("Введите кол-во результатов для получения: "))
    query = input("Введите ключ для получения: ")
    data = get_random_book(NUM_RESULTS=num_results, QUERY=query)


    if data:
        print(f"\n данные о {'num_results'}  ")
        user_info = extract_user_info(data)
        print(get_user_info_table(user_info=user_info))
    else:
        print("не удалось получить данные о API")

if __name__ == "__main__":
    main()
