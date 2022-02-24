import csv

with open('./helpers/owid-covid-data.csv') as file:
    covid_data = csv.reader(file, delimiter=',', quotechar='-')
    header, *covid_data = covid_data


filter_list_by_world = list(
    filter(lambda nc: nc[2] == 'World' and nc[16], covid_data))

new_cases = list(filter(lambda nc: nc[2] == 'World' and nc[5], covid_data))


filter_list_lask_week = filter_list_by_world[-7: -1]


cases_last_days = round(float(new_cases[-1][5]))


last_week_rate_cases_list = list(
    map(lambda rate: float(rate[16]), filter_list_lask_week))


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
