

# tickets = [
#     {"id": 101, "title": "Не приходит письмо", "closed": False, "priority": "high"},
#     {"id": 102, "title": "Не загружается аватар", "closed": True, "priority": "low"},
#     {"id": 103, "title": "Ошибка оплаты", "closed": False, "priority": "high"},
#     {"id": 104, "title": "Изменить номер телефона", "closed": False, "priority": "medium"},
# ]

# print("Данные подготовлены")

# 1)Выведи обращения в формате:
#
# 101. Не приходит письмо — открыто — high
# 102. Не загружается аватар — закрыто — low
# Статус "открыто" или "закрыто" получи тернарным оператором.

# for ticket in tickets:
#     print(f"{ticket['id']}. {ticket['title']} - {'закрыто' if ticket['closed'] else 'открыто'} - {ticket['priority']}")
#

# 2)Выведи только открытые обращения с высоким приоритетом. После списка выведи их количество.
# Не создавай вручную новый список обращений. Перебери исходную коллекцию циклом.

# print("обращения с высоким приоритетом и их количество")
# count = 0
# for ticket in tickets:
#     if ticket['priority'] == 'high':
#         count += 1
#         print(ticket)
# print(count)


# 3)Поиск по идентификатору
# Пользователь вводит id обращения. Найди его и выведи название и статус.
#
# Требования:
#
# используй цикл;
# после нахождения останови цикл через break;
# если обращения нет, выведи Обращение не найдено;
# сообщение об отсутствии нельзя выводить на каждой итерации цикла.
# Подумай, как переменная found может хранить результат поиска.
# print("Поиск по идентификатору")
#
# search = int(input("Введите id: "))
#
# found = False
# for ticket in tickets:
#     if ticket['id'] == search:
#         found = True
#         print(f"Название: {ticket['title']}, Статус: {'закрыто' if ticket['closed'] else 'открыто'}")
#         break
#
# if not found:
#     print("Обращение не найдено")


# 4) Изменение состояния
# Пользователь вводит id. Найди обращение и измени closed на True.
#
# После изменения выведи:
#
# Обращение «Ошибка оплаты» закрыто
# Если обращение уже закрыто, выведи отдельное сообщение. Если id не найден, также сообщи об этом.

# search = int(input("Введите id: "))
# found = False
# for ticket in tickets:
#     if ticket['id'] == search:
#         found = True
#         if ticket['closed']:
#             print(f"Обращение «{ticket['title']}» уже закрыто")
#         else:
#             ticket["closed"] = True
#             print(f"Обращение «{ticket['title']}» закрыто")
#         break
# if not found:
#     print("Обращение не найдено")


# 5) Изменение приоритета
# Пользователь вводит:
#
# id обращения;
# новый приоритет.
# Допустимые значения: low, medium, high.
#
# Алгоритм:
#
# Проверить, допустим ли новый приоритет.
# Если нет — вывести ошибку и не выполнять поиск.
# Если допустим — найти обращение.
# Изменить его приоритет.
# Сообщить об успешном изменении или отсутствии обращения.

# search_id = int(input("Введите id: "))
# new_priority = input("Введите новый приоритет (low, medium, high): ")
#
# if new_priority not in ["low", "medium", "high"]:
#     print("Ошибка: недопустимый приоритет")
# else:
#     found = False
#     for ticket in tickets:
#         if ticket['id'] == search_id:
#             found = True
#             ticket['priority'] = new_priority
#             print(f"Приоритет обращения «{ticket['title']}» изменён на {new_priority}")
#             break
#
#     if not found:
#         print("Обращение не найдено")


# 6) Статистика
# Посчитай и выведи:
#
# общее количество обращений;
# количество открытых;
# количество закрытых;
# количество обращений высокого приоритета;
# процент закрытых обращений.
# Процент округли до одного знака после запятой.

# all_tickets_count = len(tickets)
# open_count = 0
# close_count = 0
# high_priority_count = 0
# for ticket in tickets:
#     if ticket['closed']: open_count += 1
#     if not ticket['closed']: close_count += 1
#     if ticket['priority'] == 'high': high_priority_count += 1
#
# print(f"Общее количество {all_tickets_count}")
# print(f"Количество открытых {open_count}")
# print(f"Количество закрытых {close_count}")
# print(f"Количество с высоким приоритетом {high_priority_count}")
# print(f"Процент закрытых обращенйи {close_count / all_tickets_count * 100:.1f}%")


# Мини-система управления обращениями
# На основе списка tickets создай программу с меню:
# 1. Показать все обращения
# 2. Показать открытые обращения
# 3. Найти обращение по ID
# 4. Закрыть обращение
# 5. Добавить обращение
# 0. Завершить программу
# Требования
# меню работает в цикле while;
# программа запрашивает команду пользователя;
# каждая команда обрабатывается отдельной веткой if/elif;
# новое обращение добавляется как словарь;
# id нового обращения не должен повторять существующий;
# новое обращение по умолчанию открыто;
# неправильная команда не завершает программу;
# команда 0 завершает программу;
# поиск и изменение выполняются циклом по списку словарей;
# при отсутствии объекта выводится понятное сообщение.
# Пока не используй функции — они будут темой следующего занятия.

tickets = [
    {"id": 101, "title": "Не приходит письмо", "closed": False, "priority": "high"},
    {"id": 102, "title": "Не загружается аватар", "closed": True, "priority": "low"},
    {"id": 103, "title": "Ошибка оплаты", "closed": False, "priority": "high"},
    {"id": 104, "title": "Изменить номер телефона", "closed": False, "priority": "medium"},
]

end_of_cycle = True

while end_of_cycle:
    print("1. Показать все обращения")
    print("2. Показать открытые обращения")
    print("3. Найти обращение по ID")
    print("4. Закрыть обращение")
    print("5. Добавить обращение")
    print("0. Завершить программу")
    input_number = input("Выберите пункт: ")
    if input_number not in ["0", "1", "2", "3", "4", "5"]:
        print("Введен не корректное число")

    if input_number == "0":
        print("Программа завершена")
        break

    if input_number == "1":
        if not tickets:
            print("Список обращений пуст")
        for ticket in tickets:
            print("Список всех обращений")
            print(f"Название: {ticket['title']}, Статус: {'закрыто' if ticket['closed'] else 'открыто'}, Приоритет - ticket['priority']")
        break

    if input_number == "2":
        print("Список закрытых обращений:")
        found = False
        for ticket in tickets:
            if ticket['closed']:
                found = True
                print(f"Название: {ticket['title']}, Статус: {'закрыто' if ticket['closed'] else 'открыто'}, Приоритет - ticket['priority']")
        if found:
            print("Список закрытых обращений пуст")
        break

    if input_number == "3":
        input_id = "Введите id"
        found = False
        for ticket in tickets:
            if ticket['id'] == input_id:
                found = True
                print(f"Название: {ticket['title']}, Статус: {'закрыто' if ticket['closed'] else 'открыто'}, Приоритет - ticket['priority']")
                break
        if not found:
            print("Обращение не найдено")
        break

    if input_number == "4":
        search_id = int(input("Введите id: "))
        found = False
        for ticket in tickets:
            if ticket['id'] == search_id:
                found = True
                if ticket['closed']:
                    print("Обращение уже закрыто")
                else:
                    ticket['closed'] = True
                    print(f"Обращение «{ticket['title']}» закрыто")
                break
        if not found:
            print("Обращение не найдено")
        break


    if input_number == "5":
        new_id = int(input("Введите id нового обращения: "))

        id_exists = False
        for ticket in tickets:
            if ticket['id'] == new_id:
                id_exists = True
                break

        if id_exists:
            print("Обращение с таким id уже существует")
        else:
            title = input("Введите название: ")
            priority = input("Введите приоритет (low, medium, high): ")

            if priority not in ["low", "medium", "high"]:
                print("Недопустимый приоритет. Обращение не добавлено")
            else:
                tickets.append({
                    "id": new_id,
                    "title": title,
                    "closed": False,
                    "priority": priority
                })
                print(f"Обращение «{title}» добавлено")
        break







