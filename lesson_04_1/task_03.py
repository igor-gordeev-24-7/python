valid_temps = []
error_count = 0

with open('data/temperatures.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        try:
            temp = int(line)
            valid_temps.append(temp)
        except ValueError:
            error_count += 1

if valid_temps:
    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = sum(valid_temps) / len(valid_temps)
    above_zero = sum(1 for t in valid_temps if t > 0)

    print("Корректные температуры:", valid_temps)
    print(f"Минимальная: {min(valid_temps)}")
    print(f"Максимальная: {max(valid_temps)}")
    print(f"Среднее: {sum(valid_temps) / len(valid_temps):.2f}")
else:
    print("Корректных температур не найдено")

print(f"Количество ошибочных строк: {error_count}")
print(f"Количество значений выше нуля: {above_zero if valid_temps else 0}")

