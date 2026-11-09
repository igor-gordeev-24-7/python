def save_expedition_report(planet_name: str, commander_name: str, expedition_result: str) -> None:
    with open('data/expedition.txt', 'w', encoding='utf-8') as expedition:
        expedition.write("БОРТОВОЙ ЖУРНАЛ\n")
        expedition.write(f"Планета: {planet_name}\n")
        expedition.write(f"Командир: {commander_name}\n")
        expedition.write(f"Результат: {expedition_result}")

def main() -> None:
    planet_name = input("Введите название планеты: ")
    commander_name = input("Введите имя командира: ")
    expedition_result = input("Введите результат исследования: ")

    save_expedition_report(planet_name, commander_name, expedition_result)
    print("Отчёт сохранён")

if __name__ == '__main__':
    main()

