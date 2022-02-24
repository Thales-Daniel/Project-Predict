from reader import last_week_rate, aleatory_negative_rate,  cases_last_days
from random import choice
from media import media_elements_list


def predict(days):
    list_return = []
    media_day = media_elements_list(last_week_rate)
    for index in range(1, days + 1):
        media_day += choice(aleatory_negative_rate)
        new_cases = cases_last_days * media_day
        string_result = f'{index} -> {round(new_cases)}'
        list_return.append(string_result)
        print(f'{index} -> {round(new_cases)}')
    return list_return


if __name__ == '__main__':
    days = input('Numero de Dias: ')
    if days.isdigit() and int(days) > 0:
        predict(int(days))
    else:
        print('Apenas numeros maiores que 0!!')
