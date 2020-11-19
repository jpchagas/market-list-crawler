from datetime import date

today = date.today()


def current_date():
    return today.strftime("%d-%m-%Y")