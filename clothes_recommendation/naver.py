from bs4 import BeautifulSoup
import requests


# 네이버 날씨 크롤링
def get_minmax_temperature(ui):
    url = f'https://search.naver.com/search.naver?query={ui.region}날씨'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weather = soup.find('div', {'class': 'graph_inner _hourly_weather'})

    temperature_list = []

    # 시간 및 온도
    for i in weather.find_all('li'):
        time = i.find('dt', {'class': 'time'}).text
        degree = i.find('dd', {'class': 'degree_point'}).text

        if time == '내일':
            break

        time = int(time.strip('시'))

        if ui.departure_time <= time <= ui.arrival_time:

            temperature_list.append(degree)

    min_temp = min(temperature_list)

    max_temp = max(temperature_list)

    return max_temp, min_temp
