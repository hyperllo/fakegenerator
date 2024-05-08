from faker import Faker
from prettytable import PrettyTable
from datetime import datetime, timedelta

fake = Faker('ru_RU')

table = PrettyTable(["Имя", "Адрес", "Номер кредитной карты", "Срок действия карты", "CVV", "Провайдер карты", "Дата рождения", "Возраст"])

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
    credit_card_number = fake.credit_card_number()
    row = [
        fake.name(),
        address_with_city,
        credit_card_number,
        fake.credit_card_expire(),
        credit_card_number[-3:],
        fake.credit_card_provider(),
        birth_date,
        age
    ]
    table.add_row(row)
    table.add_row(["-" * 20] * len(table.field_names))

print(table)