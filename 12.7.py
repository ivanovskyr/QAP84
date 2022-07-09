per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
a = list(map(float, per_cent.values()))
deposit = [i*money for i in a]
print(deposit, '\nВаш максимальный доход по вкладу составит: ', max(deposit))