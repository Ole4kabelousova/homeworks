# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!


x = int(input('Введите номер месяца:'))
if 1 <= x <= 12:
    if x == 1:
        print('Вы ввели январь.')
    if x == 2:
        print('Вы ввели февраль.')
    if x == 3:
        print('Вы ввели март.')
    if x == 4:
        print('Вы ввели апрель.')
    if x == 5:
       print('Вы ввели май.')
    if x == 6:
       print('Вы ввели июнь.')
    if x == 7:
       print('Вы ввели июль.')
    if x == 8:
       print('Вы ввели август.')
    if x == 9:
       print('Вы ввели сентябрь.')
    if x == 10:
       print('Вы ввели октябрь.')
    if x == 11:
       print('Вы ввели ноябрь.')
    if x == 12:
       print('Вы ввели декабрь.')
    if x in (1, 3 ,5, 7, 8, 10, 12):
        print(31, 'дней')
    elif x in (4, 6, 9, 11):
        print(30, 'дней')
    elif x == 2:
        print(28, 'дней')
else:
  print('Такого месяца нет!')