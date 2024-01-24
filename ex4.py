from datetime import datetime, timedelta

def get_upcoming_birthday(users):
    today = datetime.today().date()
    upcoming_birthday = []


    for user in users:
        # Конвертуємо дату народження у форматі рядка у datetime об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо дату народження в цьому році
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        # Якщо день народження вже минув в цьому році, розглянемо дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()

        # Визначемо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_this_year - today).days

        # Перевірка чи припадає день народження на вихідний 
        if 0 <= days_until_birthday <= 7:
            # Якщо так то переносимо його на наступний понеділок 
            if birthday_this_year.weekday() in [5, 6]:
            
                congratulation_date = birthday_this_year + timedelta(days=(7-birthday_this_year.weekday()))

            else:
                congratulation_date = birthday_this_year


            # Додаємо ім'я користувача та дату привітання до нашого списку
            upcoming_birthday.append({
                "name":user["name"],
                "congratulation_date":congratulation_date.strftime("%Y,%m,%d")
            })    

    return upcoming_birthday



# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anton Stoliarchuk", "birthday": "1998.01.26"}
]

upcoming_birthdays = get_upcoming_birthday(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)