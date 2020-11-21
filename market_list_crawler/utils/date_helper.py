from datetime import date, datetime
import calendar

today = date.today()


def current_date():
    return today.strftime("%d-%m-%Y")

def string_date(str_date):
    return datetime.strptime(str_date, '%d-%m-%Y').date()

def get_tue_thu():
    print(calendar.day_name[today.weekday()])