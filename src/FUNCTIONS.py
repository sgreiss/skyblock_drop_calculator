def calculate_chance(base_chance: float, magic_find: float, pet_luck: float, use_pet_luck: bool) -> float:
    if use_pet_luck:
        return base_chance * (1 + ( (magic_find +pet_luck) / 100) )
    else:
        return base_chance * (1 + ( (magic_find) / 100) )