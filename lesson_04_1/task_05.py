def add_to_file(file_name: str, names: list[str]):
    with open(file_name, mode='a', encoding='utf-8') as row:
        for name in names:
            print(name)
            row.write(name + "\n")
        row.write(f"Количество уникальных участников: {len(names)}\n")




with open('data/participants.txt', 'r') as f:
    participants = f.readlines()

new_participants = []
for participant in participants:
    name = participant.strip().lower()
    if name == "":
        continue
    if name in new_participants:
        continue
    new_participants.append(name)

results = []
for participant in new_participants:
    words = participant.split()
    result = " ".join(word[0].upper() + word[1:] for word in words)
    results.append(result)

results.sort()

add_to_file("data/participants_clean.txt", results)

