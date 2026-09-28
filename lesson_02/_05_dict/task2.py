# Задача 12. Перебор словаря
# Используя словарь из предыдущей задачи:
device = {
    "name": "Office-PC",
    "ram": 16,
    "online": True,
}

# Выведи все ключи.
# print(device.keys())

# Выведи все значения.
# print(device.values())

# Выведи пары в формате name: Office-PC.
for key, value in device.items():
    print(f"{key}: {value}")

# Используй keys(), values() и items().


