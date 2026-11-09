import json
from pathlib import Path

JSON_PATH = Path("data/expenses.json")

def read_str(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не может быть пустым.\n")


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Нужно число.\n")
            continue
        if value <= 0:
            print("Сумма должна быть положительной.\n")
            continue
        return value


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Нужно целое число.\n")

def get_data() -> list:
    with open('data/settings.json') as infile:
        data = json.load(infile)
        return data

def load_expenses(path: Path = JSON_PATH):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as err:
        print(f"Файл {path} повреждён: {err}. Начинаю с пустого списка.")
        return []

    if not isinstance(data, list):
        print(f"Ожидался список, получен {type(data).__name__}. Начинаю с пустого списка.")
        return []

    return [item for item in data if isinstance(item, dict)]


def save_expenses(expenses: list[dict], path: Path = JSON_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)


def next_free_id(expenses: list[dict]) -> int:
    used = {e.get("id") for e in expenses if isinstance(e.get("id"), int)}
    candidate = max(used, default=0) + 1
    while candidate in used:
        candidate += 1
    return candidate

def add_expense(expenses: list[dict], path: Path = JSON_PATH) -> dict:
    title = read_str("Название: ")
    category = read_str("Категория: ")
    amount = read_float("Сумма: ")

    expense = {
        "id": next_free_id(expenses),
        "title": title,
        "category": category,
        "amount": amount,
    }

    expenses.append(expense)
    save_expenses(expenses, path)
    return expense


def delete_expense(expenses: list[dict], expense_id: int, path: Path = JSON_PATH) -> dict |None:
    for i, e in enumerate(expenses):
        if e.get("id") == expense_id:
            removed = expenses.pop(i)
            save_expenses(expenses, path)
            return removed
    return None


def find_by_category(expenses: list[dict], category: str) -> list[dict]:
    query = category.strip().lower()
    if not query:
        return []
    return [
        e for e in expenses
        if isinstance(e.get("category"), str) and e["category"].strip().lower() == query
    ]

def total_amount(expenses: list[dict]) -> float:
    return sum(e["amount"] for e in expenses if isinstance(e.get("amount"), (int, float)))


def largest_expense(expenses: list[dict]) -> dict | None:
    if not expenses:
        return None
    return max(expenses, key=lambda e: e.get("amount", 0))


def print_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("Расходов нет.\n")
        return
    for e in expenses:
        print(f'#{e["id"]}  {e["title"]}  |  {e["category"]}  |  {e["amount"]:.2f} ₽')
    print()


def main() -> None:
    expenses = load_expenses()

    while True:
        print("1. Показать все расходы")
        print("2. Добавить расход")
        print("3. Найти расходы по категории")
        print("4. Показать общую сумму")
        print("5. Показать самую крупную покупку")
        print("6. Удалить расход")
        print("0. Выйти\n")

        choice = read_int("Введите пункт меню: ")

        if choice == 1:
            print_expenses(expenses)

        elif choice == 2:
            added = add_expense(expenses)
            print(f'Добавлено: #{added["id"]} {added["title"]}\n')

        elif choice == 3:
            category = read_str("Категория: ")
            found = find_by_category(expenses, category)
            if found:
                print_expenses(found)
            else:
                print("Ничего не найдено.\n")

        elif choice == 4:
            print(f"Общая сумма: {total_amount(expenses):.2f} ₽\n")

        elif choice == 5:
            best = largest_expense(expenses)
            if best:
                print(f'Самая крупная покупка: {best["title"]} — {best["amount"]:.2f} ₽\n')
            else:
                print("Список пуст.\n")

        elif choice == 6:
            expense_id = read_int("Введите id для удаления: ")
            removed = delete_expense(expenses, expense_id)
            if removed:
                print(f'Удалено: #{removed["id"]} {removed["title"]}\n')
            else:
                print(f"Расход с id={expense_id} не найден.\n")

        elif choice == 0:
            print("До свидания.")
            break

        else:
            print("Нет такого пункта.\n")


if __name__ == "__main__":
    main()