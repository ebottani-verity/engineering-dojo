from typing import List


class Pokemon:
    def __init__(self, id: int, name: str, type: List[str], level: int):
        self.id = id
        self.name = name
        self.type = type
        self.level = level


class ModifiedPokemon:
    def __init__(self, id: int, name: str, type: list, level: int, modifiers: dict):
        self.id = id
        self.name = name
        self.type = type
        self.level = level
        self.modifiers = modifiers
