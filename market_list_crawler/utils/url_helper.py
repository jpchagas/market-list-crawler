from datetime import date, datetime, timedelta
import calendar


def generate_url_bulk():
    urls = []
    prefix = r'http://ceasa.rs.gov.br/tabcotacao/'
    for data in get_dates():
        if data > date(2020, 1, 8):
            url = prefix + data.strftime('%d-%m-%Y') + '/'
        elif data == date(2020, 1, 8):
            url = prefix + '2339' + '/'
        else:
            url = prefix + 'cotacao-' + data.strftime('%d-%m-%Y') + '/'
        urls.append(url)

    return urls


def get_dates():
    days_list = []
    begin_date = date(2019, 11, 28)
    end_date = date(2020, 11, 21)

    delta = end_date - begin_date

    for i in range(delta.days + 1):
        day = begin_date + timedelta(days=i)
        #if get_weekday_name(day) == 'Tuesday' or get_weekday_name(day) == 'Thursday':
        days_list.append(day)
    return days_list