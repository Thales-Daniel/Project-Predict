import csv
import numpy as np

with open('owid-covid-data.csv') as file:
    covid_data = csv.reader(file, delimiter=',', quotechar='-')
    header, *covid_data = covid_data


filter_list_by_world = list(
    filter(lambda nc: nc[2] == 'World' and nc[16], covid_data))

new_cases = list(filter(lambda nc: nc[2] == 'World' and nc[5], covid_data))


cases_last_week = filter_list_by_world[-7: -1]


cases_last_days = round(float(new_cases[-1][5]))


last_week_rate = list(
    map(lambda rate: float(rate[16]), cases_last_week))

standart_desviation = np.std(last_week_rate)
