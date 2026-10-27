import json

def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("\nНекорректный ввод: нужно целое число\n")

def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("\nНекорректный ввод: нужно целое число\n")

def get_games() -> list:
    with open('data/games.json') as infile:
        games = json.load(infile)
        return games

def add_game(game: dict):
    games = get_games()
    games.append(game)
    with open('data/games.json', mode="w", encoding="utf-8") as outfile:
        json.dump(games, outfile, ensure_ascii=False, indent=4)

def delete_game(game_id: int) -> bool:
    games = get_games()
    filtered = [g for g in games if g["id"] != game_id]

    if len(filtered) == len(games):
        return False

    with open('data/games.json', mode="w", encoding="utf-8") as outfile:
        json.dump(filtered, outfile, ensure_ascii=False, indent=4)

    return True

def change_status(game_id: int) -> bool:
    games = get_games()
    for game in games:
        if game["id"] == game_id:
            game["available"] = not game["available"]

            with open('data/games.json', mode="w", encoding="utf-8") as outfile:
                json.dump(games, outfile, ensure_ascii=False, indent=4)

            return True

    return False


end = False
while not end:
    print("1. Показать все игры")
    print("2. Добавить игру")
    print("3. Изменить доступность")
    print("4. Удалить игру")
    print("0. Выйти\n")

    choice = read_int("Введите пункт меню: ")


    if choice == 1:
        games = get_games()
        for game in games:
            print(f'ID: {game["id"]}')
            print(f'Название: {game["title"]}')
            print(f'Жанр: {game["genre"]}')
            print(f'Игроков: {game["players"]}')
            print(f'Рейтинг: {game["rating"]}')
            print(f'Доступна: {"да" if game["available"] else "нет"}\n')


    if choice == 2:
        games = get_games()

        existing_ids = {g["id"] for g in games}
        game_id = max(existing_ids, default=0) + 1

        while game_id in existing_ids:
            game_id += 1

        title = input("Введите название: ").strip()
        genre = input("Введите жанр: ").strip()
        players = read_int("Введите количество игроков: ")
        rating = read_float("Введите рейтинг: ")
        game = {
            "id": game_id,
            "title": title,
            "genre": genre,
            "players": players,
            "rating": rating,
            "available": True,
        }
        add_game(game)


    if choice == 3:
        id = read_int("Введите id для смены статуса: ")
        status = change_status(id)
        if not status:
            print(f"Статус не изменен")

        print(f"Статус по id {id}, изменен")



    if choice == 4:
        id = read_int("Введите id для удаления: ")
        removed = delete_game(id)
        if removed:
            print(f'Удалена игра: {removed["title"]} (id={id})\n')
        else:
            print(f"Игра с id={id} не найдена.\n")

    if choice == 0:
        print("Программа завершена")
        end = True