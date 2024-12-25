import requests
import pprint
import json
from prettytable import PrettyTable
import configparser

def get_api_key(filename= "requests/config.ini"):
    conf = configparser.ConfigParser()
    conf.read(filename)
    my_api_key=conf.get('api', 'api_key')
    print(f"ваш ключ - {my_api_key}")

    return my_api_key

def get_weather_data(city="Moscow", api_key=""):

    if api_key == "":
        api_key = get_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ошибка при запросе: {e}")
        return None
    

    
def extract_weather_info(data):

    if data:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        return (city_name , temperature , humidity , weather_description , wind_speed , pressure)
    return None



# pprint.pprint(requests.get(url="https://restcountries.com/v3.1/name/Russia").json())
def get_weather_info_table(weather_info):
    table = PrettyTable()
    table.field_names = ["город", " Температура" , " Влажность", "описание" , "Скорость ветра", "Давление"]
    table.add_row(weather_info)
    return table

def main():
    city = (input("Введите название города: "))
    data = get_weather_data(city)

    if data:
        weather_info = extract_weather_info(data)
        print(get_weather_info_table(weather_info=weather_info))
    else:
        print("не удалось найти api ")
