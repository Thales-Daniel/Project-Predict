def media_elements_list(list_rates):
    if isinstance(list_rates, list) is False:
        return "Enter a list of numbers"
    return round(sum(list_rates) / len(list_rates), 2)
