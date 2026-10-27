import json
from pathlib import Path

settings = {
    "language": "ru",
    "theme": "dark",
    "notifications": True,
    "items_per_page": 20,
    "favorite_sections": [
        "Обучение",
        "Проекты"
    ]
}

path = Path("data/settings.json")
path.parent.mkdir(parents=True, exist_ok=True)

with open(path, mode="w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=4)

with open(path, mode="r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Тема: ", loaded["theme"])
print("Язык: ", loaded["language"])
print("Избранные разделы:")
for section in loaded["favorite_sections"]:
    print(" -", section)

print("Тип загруженного значения:", type(loaded))

