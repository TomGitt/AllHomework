
# # text = input('Введіть вашу криву строку ')
# text = (f'434dfdfANYdfdfdf4545').isdigit()
# # for final in [5.5, 'fg']:
# #     print(final)
# print(range(12))
# for day in range(12):
#     print(day)®†©√ç√πøø˚∆∆˜∫√√ç≈Ωåœ∑´r∑´r´®d
# list_week_temperat = input('tttt')
# list_week_temperat = list_week_temperat.split()
#
#
# for dayt in range(1, 8):
#     float(dayt)
#     temp = float(input(f'day {dayt}: enter temperat >>> '))
#     list_week_temperat.append(temp)
#     # print(list_week_temperat)
#     print(sum(dayt) + (list_week_temperat))
# Как вывести на экран год и день недели с помощью strftime()
# import datetime #Импорт модуля
# x = datetime.datetime. now() #Вызов метода now из класса datetime.
# print(x.year) #Вывод на экран значения текущего года
# print(x. strftime("%A")) #Отображение на экране значения текущего дня недели

ukraine_cities = ['Odessa', 'Lviv', 'Dnipro', ]
city_list_kyiv_style = []
expenses = []
other = []
last_city = []
some_trash_list = ['Lviv', 1000, 'Leviy4el', 'Odessa', 800, 'Dnipro', 500, ['Igor', 'sahsa']]

for value in some_trash_list:
    # if type(value) == str:
    if isinstance(value, str) and value in ukraine_cities:
        city_list_kyiv_style.append(value)

    # if type(value) == int or type(value) == float:
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        expenses.append(value)
    else:
        other.append(value)
print(city_list_kyiv_style)
print(expenses)
# print('f' in ukraine_cities)
# print(5 in ukraine_cities)
# print('Dnipro' in ukraine_cities)

odessa_data_destination = ['Dnipro', 'Donetsk', 'Zaporizja']

city_list_kyiv_style.extend(odessa_data_destination)
city_list_kyiv_style.sort()
print(city_list_kyiv_style)

# city_list_kyiv_style.pop()
print(last_city)
city_list_kyiv_style.pop(2)

print(city_list_kyiv_style[:2])
print(city_list_kyiv_style[:])
if city_list_kyiv_style:
    print('fireshow: ', city_list_kyiv_style[-1])

city_list_kyiv_style.insert(3, 'Izum')
print(city_list_kyiv_style)
