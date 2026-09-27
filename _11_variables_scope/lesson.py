DEFAULT_LEVEL_EXPERIENCE = 200

def is_leveled_up(*, current_exp: int, gained_exp: int) -> bool:
    total = current_exp + gained_exp
    level_up = False

    if total >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_exp=150, gained_exp=60))
print(is_leveled_up(current_exp=10, gained_exp=60))
