from datetime import datetime, timedelta
from collections import defaultdict


DAYS = 6
MONDAY_INDEX = 7

users = [
            {
                "name":"Bill", 
                "birthday":"1998-02-18"
            },
            {
                "name":"Giil", 
                "birthday":"1999-02-22"
            },
            {
                "name":"Till",
                "birthday":"2000-02-19"
            }
        ]
def get_birthdays_this_year(current_date, users):

    dict_users = defaultdict(list)
    list_users = []
    
    for user in users:

        #current_date = datetime.now().date()
        birthday_date = datetime.strptime(user["birthday"], '%Y-%m-%d').date()
        current_birthday = birthday_date.replace(year=current_date.year)
        dict_users[current_birthday].append(user["name"])

    return dict_users

def change_weekends_birthdays(date, dict_users, names):
        
        date = date + timedelta(days = MONDAY_INDEX - date.weekday())
        return date
        

def birthdays_filter(date, current_date, days):
    
    if current_date <= date <= current_date + timedelta(days):
        return date


def main():

    current_date = datetime.now().date()#

    dict_users = get_birthdays_this_year(current_date, users)

    for date, names in list(dict_users.items()):

        if date.weekday() in (5, 6):

            dict_users.pop(date)
        
            date = change_weekends_birthdays(date, dict_users, names)

            dict_users.update({date:names})
        
        date = birthdays_filter(date, current_date, DAYS)
            
        print(f'{date.strftime("%A")}: {", ".join(names)}')
                    
if __name__ == '__main__':
    main()
