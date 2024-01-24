from datetime import datetime, timedelta

def get_upcoming_birthday(users):
    
    today = datetime.today().date()
    upcoming_birthday = []


    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()


        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()


        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()


        days_until_birthday = (birthday_this_year - today).days



        if 0 <= days_until_birthday <= 7:

            if birthday_this_year.weekday() in [5, 6]:

                congratulation_date = birthday_this_year + timedelta(days=(7-birthday_this_year.weekday()))


            else:
                congratulation_date = birthday_this_year



            upcoming_birthday.append({
                "name":user["name"],
                "congratulation_date":congratulation_date.strftime("%Y,%m,%d")
            })    


    return upcoming_birthday






users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anton Stoliarchuk", "birthday": "1998.01.26"}
]

upcoming_birthdays = get_upcoming_birthday(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
