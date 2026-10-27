import json
from pathlib import Path

TXT_PATH = Path("data/courses.txt")
JSON_PATH = Path("data/courses.json")

def read_txt(path: Path) -> list[tuple[int, str]]:
    try:
        with open(path, encoding="utf-8") as f:
            return list(enumerate(f, start=1))
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
        return []

def parse_line(line_num: int, line: str) -> tuple[dict | None, str | None]:
    parts = [p.strip() for p in line.split(";")]

    if len(parts) != 3:
        return None, f"строка {line_num}: ожидалось 3 поля, получено {len(parts)}"

    title, students_raw, rating_raw = parts

    if not title:
        return None, f"строка {line_num}: пустое название"

    try:
        students = int(students_raw)
    except ValueError:
        return None, f"строка {line_num}: студенты «{students_raw}» не число"

    try:
        rating = float(rating_raw)
    except ValueError:
        return None, f"строка {line_num}: рейтинг «{rating_raw}» не число"

    return {
        "title": title,
        "students": students,
        "rating": rating,
    }, None

def convert(text_path: Path = TXT_PATH, json_path: Path = JSON_PATH) -> tuple[int, int]:
    lines = read_txt(text_path)

    courses = []
    skipped = 0

    for line_num, raw in lines:
        if not raw.strip():
            continue

        course, error = parse_line(line_num, raw)
        if course is None:
            print(f"Пропущено: {error}")
            skipped += 1
            continue

        courses.append(course)

    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)

    return len(courses), skipped

if __name__ == "__main__":
    saved, skipped = convert()
    print(f"\nСохранено: {saved}\n")
    print(f"Пропущено: {skipped}\n")



