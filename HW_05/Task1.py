# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections
import statistics

print('Посчитаем среднюю прибыль для предпрятий и выведем компании, у которых она больше или меньше средней.')
count_companies = int(input('Введите, пожалуйста, количество предприятий:   '))
Company = collections.namedtuple('Company', ['name', 'quarter1', 'quarter2', 'quarter3', 'quarter4', 'profit'])
# заводим массив под данные о прибыли компаний и о названии:
database = []
# отдельно сразу будем сохранять прибыли, для подсчета среднего значения:
profits = []
# создаем массив данных:
for company in range(count_companies):
    profile = list(input(
        'Через точку с запятой (;): название компании; прибыль за первый кваратал; второй; третий; четвёртый--> ').split(
        ';'))
    # считаем годовую прибыль предприятия:
    profit = (float(profile[1]) + float(profile[2]) + float(profile[3]) + float(profile[4]))
    # заводим namedtuple под вводимые данные и подсчитанную годовую прибыль:
    company = Company(name=profile[0], quarter1=profile[1], quarter2=profile[2], quarter3=profile[3],
                      quarter4=profile[4], profit=profit)

    database.append(company)
    profits.append(company.profit)
# ищем среднюю прибыль
avg = statistics.mean(profits)
# заводим массивы под компании с прибылью выше средней, ниже средней и равной средней:
succeeded = []
failed = []
average = []
# сортируем компании по средней прибыли:
for company in database:
    if company.profit > avg:
        succeeded.append(company.name)
    elif company.profit < avg:
        failed.append(company.name)
    else:
        average.append(company.name)

print(f'Средняя годовая прибыль по компаниям: {avg}')
# красивенько выводим:
if len(succeeded) > 0:
    print('Выше среднегодовой по компаниям: ')
    for company in succeeded:
        print(f'{company}')
if len(failed) > 0:
    print('Ниже срежнегодовой по компаниям:')
    for company in failed:
        print(f'{company}')
if len(succeeded) == 0 and len(failed) == 0 and len(average) > 0:
    print(f'Среднегодовая прибыль одинаковая у всех этих компаний:')
    for company in average:
        print(f'{company}')

########################
# Тестовые данные
########################
# taart; 10; 9; 8; 7
# maart; 11; 19; 18; 17
# baart; 21; 29; 28; 27
########################
# taart; 5; 15; 1; 19
# maart; 11; 9; 12; 8
# baart; 0; 0; 0; 40
########################
# taart; 0; 1; 1; 0
# maart; 0; 0; 1; 0
# baart; 0; 1; 0; 0
# waart; 0; 1; 1; 1
# kaart; 1; 0; 1; 1
