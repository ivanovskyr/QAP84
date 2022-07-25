try:
    tickets = int(input("Добро пожаловать на конференци!\nСколько билетов Вам необходимо?: "))
    age = {}
    count = 0
    for i in range(tickets):
        age[i] = int(input(f"Введите возраст {i+1} посетителя: "))
        if 18 <= age[i] <= 25:
            count += 990
            print("Стоимость билета составит 990 рублей")
        elif age[i] > 25:
            count += 1390
            print("Стоимость билета составит 1390 рублей")
        else:
            print("Посетители до 18 лет проходят бесплатно")
        print(f"\nСумма Вашего заказа составляет: {count}")
    if tickets > 3:
        count = count * 0.9
        print(f"\nСумма заказа с учётом скидки 10% составляет: {count}")
except ValueError:
    print("Попробуйте заново с корректными данными!")
