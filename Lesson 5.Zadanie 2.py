# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('text_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n{content}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле: \n{len(content)}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
my_file = open('text_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
