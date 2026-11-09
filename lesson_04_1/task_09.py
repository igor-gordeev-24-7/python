import json


def load_devices(path: str = "devices.json") -> list:
    try:
        with open(path, encoding="utf-8") as infile:
            return json.load(infile)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as err:
        print(f"Файл {path} повреждён: {err}")
        return []