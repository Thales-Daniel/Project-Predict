import csv

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


aleatory_negative_rate = [
    -0.031,
    -0.022,
    -0.012,
    -0.023,
    -0.013,
    -0.011,
    0.001,
    0.011,
]

aleatory_casual_cases = [10, 20, 33, 2, 3, 13, 7, 27, 22, 12, 8, 10]
