from faker import Faker
from prettytable import PrettyTable
from datetime import datetime, timedelta
import random
import string
from transliterate import translit

fake = Faker('ru_RU')

table = PrettyTable(["Имя", "Адрес", "Почта", "Пароль", "Номер кредитной карты", "Срок действия карты", "CVV", "Провайдер карты", "Дата рождения", "Возраст"])

file_path = "about.txt"

with open(file_path, "w", encoding="utf-8") as file:
    for _ in range(5):
        city = fake.city()
        address_with_city = city + ", " + fake.address()
        birth_date = fake.date_of_birth(minimum_age=16, maximum_age=90)
        age = (datetime.now().date() - birth_date).days // 365
        if age < 16:
            birth_date = datetime.now().date() - timedelta(days=16*365)
            age = 16
        elif age > 90:
            birth_date = datetime.now().date() - timedelta(days=90*365)
            age = 90
        name = fake.name().split()
        email_name = translit(random.choice(name), 'ru', reversed=True).lower()
        email_name += ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 5)))
        domain = fake.free_email_domain()
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(12, 14)))
        email = f"{email_name}@{domain}"
        credit_card_number = fake.credit_card_number()
        row = [
            ' '.join(name),
            address_with_city,
            email,
            password,
            credit_card_number,
            fake.credit_card_expire(),
            credit_card_number[-3:],
            fake.credit_card_provider(),
            birth_date,
            age
        ]
        table.add_row(row)
        table.add_row(["-" * 20] * len(table.field_names))

    table_string = table.get_string()

    file.write(table_string)

print("Все файлы сохранены в about.txt")
print("При повторной генерации данные в about.txt будут очищены")
