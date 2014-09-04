import datetime
import argparse

def parse_date(date_string):
    date_array = date_string.split("/")
    if len(date_array) != 3:
        raise Exception("Date must be of format \"MM/DD/YYYY\"!")

    try:
        month = int(date_array[0])
    except ValueError:
        raise Exception("Month must be an integer")

    try:
        day = int(date_array[1])
    except ValueError:
        raise Exception("Day must be an integer")

    try:
        year = int(date_array[2])
    except ValueError:
        raise Exception("Year must be an integer")

    try:
        return datetime.date(year,month,day)
    except ValueError as e:
        raise e
    return None

def gen_row(date):
    s = ""
    if date.weekday() == 6:
        day_of_week = "Sun"
    elif date.weekday() == 0:
        day_of_week = "Mon"
    elif date.weekday() == 1:
        day_of_week = "Tue"
    elif date.weekday() == 2:
        day_of_week = "Wed"
    elif date.weekday() == 3:
        day_of_week = "Thu"
    elif date.weekday() == 4:
        day_of_week = "Fri"
    elif date.weekday() == 5:
        day_of_week = "Sat"

    return '|' + day_of_week + '|[[' + str(date.year) + '/' + str(date.month) + '/' + str(date.day) + ']]||'

def generate_index(start_date_str, num_days_str):
    date = parse_date(start_date_str)
    delta_day = datetime.timedelta(days=1)

    try:
        num_days = int(num_days_str)
    except ValueError:
        raise Exception("number of days must be an integer")

    s = ''
    s += '!Planner\n'
    s += '|!Day|!Date|!Events|\n'

    for i in range(num_days):
        s += gen_row(date) + '\n'
        date += delta_day

    s += '----\n'
    s += '!Tasks\n'
    return s

def main():
    parser = argparse.ArgumentParser(description='Generate a tiddlywiki bullet journal index!')
    parser.add_argument('start_date', help = 'Start date formatted at "MM/DD/YYYY"')
    parser.add_argument('number_of_days', help = 'Number of days to generate')
    args = parser.parse_args()
    index = generate_index(args.start_date, args.number_of_days)
    print index

if __name__ == '__main__':
    main()
