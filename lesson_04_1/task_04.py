import sys

query = input("Введите слово или фразу для поиска: ").strip()

found_count = 0

if query == "":
    print("Пустой запрос")
    sys.exit()

query_lower = query.lower()

with open("data/meeting.txt", mode="r", encoding="utf-8") as f:
    for line_index, line in enumerate(f, start=1):
        if query_lower in line.lower():
            print(f"Строка {line_index}: {line}")
            found_count += 1

print(f"Найдено строк: {found_count}")

if found_count == 0:
    print("Совпадений не найдено")

