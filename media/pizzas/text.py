import os

# Указываем путь к папке (в данном случае — текущая папка)
folder_path = '.'

# Получаем список файлов (без папок)
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Склеиваем имена файлов через пробел
a = ' '.join(file_names)

# Выводим переменную a
print(a)