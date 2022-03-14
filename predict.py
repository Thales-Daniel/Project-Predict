from reader import Reader, Filter_reader_datas
from media import media_elements_list


def predict(days):
    data = Reader.reader_csv()
    filter_list = Filter_reader_datas(data)
    list_return = []
    media_day = media_elements_list(filter_list.get_last_week_rate())
    for index in range(1, days + 1):
        media_day -= filter_list.standard_desviation()
        new_cases = filter_list.get_cases_last_day() * media_day
        if new_cases < 0:
            new_cases = 0
        string_result = f"{index} -> {round(new_cases)}"
        list_return.append(string_result)
        print(f"{index} -> {round(new_cases)}")
    return list_return


if __name__ == "__main__":
    days = input("Numero de Dias: ")
    if days.isdigit() and int(days) > 0:
        predict(int(days))
    else:
        print("Apenas numeros maiores que 0!!")
