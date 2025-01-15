import requests
import pprint
import json
from prettytable import PrettyTable

def get_info_country(country_name=5):
    url = f"https://restcountries.com/v3.1/name{country_name}"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ошибка при запросе: {e}")
        return None
    
def extract_country_info(data):
    country_info = []

    for user in data:
        common = f"{['name']['common']}"
        capital = f"{['idd']['capital']}"
        region= f"{['idd']['region']}"
        population = f"{['population']}"
        flag= f"{['flag']}"
        languages = f"{['idd']['languages']}"
        user_info.append((common,capital , region, population, flag, languages))


# pprint.pprint(requests.get(url="https://restcountries.com/v3.1/name/Russia").json())

def main():
    country_name = (input("Введите название страны для получения информации: "))
    data = get_info_country(country_name=country_name)