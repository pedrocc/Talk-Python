import datetimedef print_header():    print('------------------------------------------')    print('              BIRTHDAY APP')    print('------------------------------------------', '\n')def get_birthday_from_user():    year = int(input('What year were you born [YYYY]? '))    month = int(input('What month were you born [MM]? '))    day = int(input('What day were you born [DD]? '))    birthday = datetime.datetime(year, month, day)    return birthdaydef compute_days_between_dates(original_date, now):    date1 = now    date2 = datetime.datetime(now.year, original_date.month, original_date.day)    dt = date1 - date2    days = int(dt.total_seconds() / 60 / 60 / 24)    return daysdef print_birthday_informatioin(days):    if days < 0:        print('Your birtday is in {} days!'.format(-days))    elif days > 0:        print('You had your birthday already this year! {} days ago'.format(days))    else:        print('Happy birthday!')    return Nonedef main():    print_header()    bday = get_birthday_from_user()    now = datetime.datetime.now()    number_of_days = compute_days_between_dates(bday, now)    print_birthday_informatioin(number_of_days)main()