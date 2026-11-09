import json
from pathlib import Path

FILE_PATH = Path("data/spacecraft.json")

def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("\nНекорректный ввод: нужно целое число\n")


def read_str(prompt: str) -> str:
    while True:
        raw = input(prompt).strip()
        try:
            return str(raw)
        except ValueError:
            print("\nНекорректный ввод: нужна строка\n")

def load_archive(path: Path) -> list[dict]:
    try:
        with open(path, encoding="utf-8") as infile:
            data = json.load(infile)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as err:
        print(f"Файл {path} повреждён: {err}")
        return []

    if not isinstance(data, list):
        print(f"Ожидался список, а получен {type(data).__name__}")
        return []

    return data

# load_archive(FILE_PATH)


def save_archive(archive: list[dict], path: Path = FILE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(archive, outfile, ensure_ascii=False, indent=4)

archive = [
    {"id": 1, "name": "Voyager 1", "country": "США",    "launch_year": 1977, "active": True},
    {"id": 2, "name": "Луна-25",   "country": "Россия", "launch_year": 2023, "active": False},
]

# save_archive(archive)


def find_by_name(name: str, path: Path = FILE_PATH) -> list[dict]:
    data = load_archive(path)

    query = name.strip().lower()
    if not query:
        return []

    return [
        item for item in data
        if isinstance(item, dict)
        and isinstance(item.get("name"), str)
        and query in item["name"].lower()
    ]

# print(find_by_name("Voyager "))

def find_by_country(country: str, path: Path = FILE_PATH) -> list[dict]:
    data = load_archive(path)

    query = country.strip().lower()
    if not query:
        return []

    return [
        item for item in data
        if isinstance(item, dict)
        and isinstance(item.get("country"), str)
        and item["country"].strip().lower() == query
    ]


# print(find_by_country(""))


def find_by_launch_year(launch_year: int, path: Path = FILE_PATH) -> list[dict]:
    data = load_archive(path)
    return [
        item for item in data
        if isinstance(item, dict)
        and item["launch_year"] > launch_year
    ]

# print(find_by_launch_year(2022))


def change_status(id: int, path: Path = FILE_PATH) -> bool:
    data = load_archive(path)
    for item in data:
        if item.get("id") == id:
            item["active"] = not item["active"]
            save_archive(data, path)
            return True
    return False

change_status(1)


def add_item(
    name: str,
    country: str,
    launch_year: int,
    active: bool,
    path: Path = FILE_PATH,
) -> dict:
    data = load_archive(path)

    existing_ids = {item.get("id") for item in data if isinstance(item, dict)}
    new_id = max((i for i in existing_ids if isinstance(i, int)), default=0) + 1
    while new_id in existing_ids:
        new_id += 1

    new_item = {
        "id": new_id,
        "name": name.strip(),
        "country": country.strip(),
        "launch_year": launch_year,
        "active": active,
    }

    data.append(new_item)
    save_archive(data, path)

    return new_item



