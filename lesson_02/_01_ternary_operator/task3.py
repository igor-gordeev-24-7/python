# Задача 3. Когда тернарный оператор не подходит
# Перепиши код через обычный if/elif/else, потому что здесь больше двух вариантов:
#
# меньше 40 — low;
# от 40 до 79 включительно — medium;
# 80 и больше — high.

load = 65
if load < 40:
    print("low")
elif load >= 40 and load <= 79:
    print("medium")
elif load >= 80:
    print("high")