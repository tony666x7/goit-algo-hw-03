import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка вхідних параметрів
    if not (1 <= min <= max <= 1000 and 1 <= quantity <= max - min + 1):
        return []
    
    # Генерація унікальних випадкових чисел
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        random_number = random.randint(min, max)
        unique_numbers.add(random_number)

    # Перетворення множини в список і відсортування
    sorted_numbers = sorted(list(unique_numbers))

    return sorted_numbers



# Приклад використання 
lottery_numbers = get_numbers_ticket(1, 49, 5)
print("Ваші лотерейні числа:", lottery_numbers)