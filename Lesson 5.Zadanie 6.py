# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def user_Predmet_stat(filename):
    result = {}
    try:
        with open(filename, 'r', encoding='utf-8') as i_File:
            for str in i_File:
                predmet = str.split(' ')[0][:-1]
                hours_lst = str.split(' ')[1:]
                dig_lst = [int(s.split('(')[0]) for s in hours_lst if s.split('(')[0].isdigit()]
                hours = sum(dig_lst)
                result[predmet] = hours
    except IOError as err:
        print(f'ERROR: Не могу открыть файл: \'{filename}\' ')
    return result


print(f' Результат: предмет и общее количество часов по нему: {type(user_Predmet_stat("text_6.txt"))}, '
      f'{user_Predmet_stat("text_6.txt")}')
