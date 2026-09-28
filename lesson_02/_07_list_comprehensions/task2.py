# Задача 16. Фильтрация имён файлов
# Дан список:
#
files = ["main.py", "notes.txt", "app.py", "photo.png", "test_app.py"]

# Создай новый список, содержащий только файлы с расширением .py.
only_py = [i for i in files if i.find(".py") > 0]
print(only_py)
