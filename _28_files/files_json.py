# import json
#
#
# data = {"name": "Mike", "age": 30, "city": "New York"}
#
# file = open('files/data.json', 'w')
# json.dump(data, file)
# file.close()
#
# file = open('files/data.json', 'r')
# loaded_data = json.load(file)
# print(loaded_data)
# file.close()

tasks = [
  "Подготовить презентацию",
  "Изучить словари",
  "Сделать домашнее задание",
]


for i in range(len(tasks)):
  print(f"{i}. {tasks[i]}")