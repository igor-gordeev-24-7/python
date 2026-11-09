events_input = ""
count = 0
while events_input != "END":
    events_input = input("Введите событие: ")
    if events_input != "END" and events_input.strip() != "":
        with open('data/events.txt', mode='a', encoding='utf-8') as events:
            events.write(f"{events_input}\n")
        count += 1
print(f"Добавлено событий: {count}")
