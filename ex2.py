from datetime import datetime

def get_days_from_today():
    try:
        # Користувач вводить дату у форматі 'РРРР-ММ-ДД'
        date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
        
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' в об'єкт datetime
        input_date = datetime.strptime(date_input, '%Y-%m-%d')
        
        # Отримуємо поточну дату
        current_date = datetime.today()

        # Розраховуємо різницю між поточною датою та заданою датою у днях
        days_difference = (current_date - input_date).days

        return days_difference
    except ValueError:
        # Обробка винятків для неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

# Виклик функції
result = get_days_from_today()
print(f"Кількість днів між введеною датою і сьогодні: {result}")
