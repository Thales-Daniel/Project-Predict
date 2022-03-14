import csv
import numpy as np


class Reader:
    @classmethod
    def reader_csv(self):
        with open("owid-covid-data.csv") as file:
            covid_data = csv.reader(file)
            header, *covid_data = covid_data
            return covid_data


class Filter_reader_datas:
    def __init__(self, data):
        self.data = data

    def filter_list_by_world(self):
        filter_list_by_world = list(
            filter(lambda nc: nc[2] == "World" and nc[16], self.data)
        )
        return filter_list_by_world

    def get_new_cases(self):
        new_cases = list(
            filter(lambda nc: nc[2] == "World" and nc[5], self.data)
        )
        return new_cases

    def get_cases_last_week(self):
        cases_last_week = self.filter_list_by_world()[-7:]
        return cases_last_week

    def get_cases_last_day(self):
        cases_last_days = round(float(self.get_new_cases()[-1][5]))
        return cases_last_days

    def get_last_week_rate(self):
        last_week_rate = list(
            map(lambda rate: float(rate[16]), self.get_cases_last_week())
        )
        return last_week_rate

    def standard_desviation(self):
        standart_desviation = np.std(self.get_last_week_rate())
        return standart_desviation
