# 5. Словари
# Словарь хранит пары ключ: значение.
#
# server = {
#     "host": "localhost",
#     "port": 8000,
#     "online": True,
# }
# data[key] — получить значение, но при отсутствии ключа возникнет KeyError;
# data.get(key) — получить значение или None;
# data.get(key, default) — получить значение или указанное значение по умолчанию;
# key in data — проверить наличие ключа.

# Задача 1. Профиль устройства
# Дан словарь:
#
device = {
    "name": "Office-PC",
    "ram": 16,
    "online": True,
}
# Выведи название устройства.
print(device["name"])

# Увеличь объём памяти до 32.
device["ram"] = 32

# Добавь ключ os со значением "Linux".
device["os"] = "Linux"

# Получи ключ ip через get(). Если ключа нет, выведи "IP не назначен".
ip = device.get("online", "IP не назначен")
print(ip)

# Проверь через in, есть ли ключ online.
var = "online" in device
print(var)

# Выведи итоговый словарь.
print(device)

