import re 

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    pattern = r'[^0-9+]' # Що саме видаляємо 
    replacement = ''     # На що замінюємо
    cleaned_phone = re.sub(pattern, replacement, phone_number)

    if not cleaned_phone.startswith("+"):
        # Додаємо міжнародний код '+38'
        cleaned_phone = "+38" + cleaned_phone.lstrip("38")


    return cleaned_phone
    

# Приклад роботи функції
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n",sanitized_numbers)