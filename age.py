import datetime
import re

today = datetime.date.today()


def ask_input():
    while True:
        given_date = input(
            'State a date in the following format: DD-MM-YYYY. Type "exit" to quit. ')
        if not given_date:
            print('No input was given. Try again.')
            continue
        if given_date.lower() == 'exit':
            print('Quitting.')
            return None
        # various types of inputs are accepted. The digits can be separated by anything but digits.
        date_template = r'(\d\d)[\D](\d\d)[\D](\d\d\d\d)'
        m = re.fullmatch(date_template, given_date)
        # below validates the input
        if m:
            day = int(m.group(1))
            month = int(m.group(2))
            year = int(m.group(3))

            try:
                user_date = datetime.date(year=year, month=month, day=day)
                # if the input is in valid format the input is returned.
                return user_date
            except ValueError:
                print('The numbers given are in invalid range. Try again. ')
                continue
        else:
            print('The date in the given format is invalid. Try again. ')


def main():
    while True:
        user_date = ask_input()
        if not user_date:
            break
        difference = today - user_date
        # difference is turned into seconds and then resulting division is the number of years
        output = difference.total_seconds() // (365.25 * 24 * 60 * 60)
        print(f'The difference in years is: {int(output)}.')


main()
