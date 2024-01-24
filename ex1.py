from datetime import datetime
# Вводимо дату у заданому форматі 
date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")  
def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати в об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
        # Отримуємо поточну дату
        current_date = datetime.today()
        # Розраховуємо різницю між поточною та заданою датою у днях
        days_difference = (current_date - input_date).days
        # Виводимо результат 
        print(f"Кількість днів між {date_input} і сьогодні: {days_difference}")
        
    # Блок обробки винятків для неправильного формату вхідних даних 
    except Exception:
        print("Неправильний формат дати. Використайте формат 'РРРР-ММ-ДД'.")
    

# Викликаємо функцію
get_days_from_today(date_input)
