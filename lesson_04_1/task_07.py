import json
games = [
    {
        "id": 1,
        "title": "The Witcher 3: Wild Hunt",
        "genre": "RPG",
        "players": 1,
        "rating": 9.8,
        "available": True
    },
    {
        "id": 2,
        "title": "Counter-Strike 2",
        "genre": "Shooter",
        "players": 10,
        "rating": 8.5,
        "available": True
    },
    {
        "id": 3,
        "title": "Minecraft",
        "genre": "Sandbox",
        "players": 8,
        "rating": 9.2,
        "available": True
    },
    {
        "id": 4,
        "title": "Elden Ring",
        "genre": "Action RPG",
        "players": 1,
        "rating": 9.6,
        "available": False
    },
    {
        "id": 5,
        "title": "Among Us",
        "genre": "Party",
        "players": 15,
        "rating": 7.9,
        "available": True
    }
]

with open('data/games.json', 'w') as outfile:
    json.dump(games, outfile, indent=4)


def get_games() -> list:
    with open('data/games.json') as infile:
        games = json.load(infile)
        return games


games = get_games()

# игры с рейтингом не ниже введённого пользователем;
def show_games_by_rating(games: list, rating: int | float) -> list[dict]:
    return [game for game in games if game["rating"] >= rating]

print(show_games_by_rating(games, 9.3))

# игру с максимальным рейтингом;
def show_game_max_rating(games: list) -> dict[str, int | float | str]:
    return max(games, key=lambda game: game["rating"])

print(show_game_max_rating(games))

def get_average_rating(games: list) -> float:
    total_rating = sum(game["rating"] for game in games)
    return total_rating / len(games)

print(get_average_rating(games))