import numpy as np
import requests
from bokeh.plotting import figure, show
from typing import List


def get_temp(own_city_name: str) -> List:
    api = "https://api.openweathermap.org/data/2.5/forecast?q=" + own_city_name + "&APPID=d438c29584f3e371f54cc81a6529daaf"

    json_data = requests.get(api).json()
    temp = []
    for i in json_data['list']:
        temp.append(float(i['main']['temp'])-273)

    return temp


def get_date(own_city_name: str) -> List:
    api = "https://api.openweathermap.org/data/2.5/forecast?q=" + own_city_name + "&APPID=d438c29584f3e371f54cc81a6529daaf"

    json_data = requests.get(api).json()
    date = []

    for i in json_data['list']:
        date.append(i['dt_txt'])

    return date


a = input('Введите город: ')


y = list((get_temp(a)))
x = np.linspace(22, 31, 40)

x_new = np.arange(22, 31, 1.385)
y_new = []

for i in range(0, len(y) - 1, 6):
    y_new.append(y[i])

plot = figure(
    title=f'Погода: {a}',
    x_axis_label='Дата',
    y_axis_label='Температура'
)
plot.dot(x_new, y_new, size=45, color='red')
plot.line(x, y, line_width=1.5)
show(plot)


