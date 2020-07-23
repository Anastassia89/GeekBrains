# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.

import json

firm_list = []
profit = 0
average_profit = 0
firm_dict = {}
firm_average_profit = {}
i = 0

with open('text_7.txt', encoding='UTF-8') as firm:
    for line in firm:
        firm_name, ownership, firm_profit, firm_costs = line.split()
        firm_dict[firm_name] = int(firm_profit) - int(firm_costs)
        if firm_dict.setdefault(firm_name) >= 0:
            i += 1
            profit = profit + firm_dict.setdefault(firm_name)
    if i != 0:
        average_profit = profit / i
    firm_average_profit = {'Средняя прибыль': round(average_profit)}
    firm_list.append(firm_dict)
    firm_list.append(firm_average_profit)
print(f'{firm_list}')

with open('text_77.json', 'w') as write_list:
    json.dump(firm_list, write_list)

firm.close()
write_list.close()
