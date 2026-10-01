# 2. Списки и их методы
# Новый пункт
# Новый пункт
# Список — изменяемая упорядоченная коллекция.
#
# Полезные операции:
#
# items.append(value)       # добавить в конец
# items.insert(index, value) # вставить по индексу
# items.remove(value)       # удалить первое совпадение
# items.pop(index)          # удалить и вернуть элемент
# len(items)                # количество элементов
# value in items            # проверка наличия

# Задача 1. Очередь загрузок
# Дана очередь файлов:
#
downloads = ["video.mp4", "report.pdf", "photo.png"]
# Выполни действия:
#
# Добавь в конец archive.zip.
# Вставь urgent.docx в начало списка.
# Удали report.pdf по значению.
# Удали последний элемент с помощью pop() и сохрани его в переменную.
# Выведи удалённый элемент, итоговый список и количество файлов.

downloads.append("archive.zip")
downloads.insert(0, "urgent.docx")
downloads.remove("report.pdf")
deleted = downloads.pop(len(downloads) - 1)
print(f"Удален файл: {deleted}")
print(f"Количество файлов: {len(downloads)}")
print(downloads)