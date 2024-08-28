from typing import List

class Pokemon:
    def __init__(self, id: int, name: str, type: List[str], level: int):
        self.id = id
        self.name = name
        self.type = type
        self.level = level

def create_mock_pikachu() -> Pokemon:
    return Pokemon(
        id=1,
        name="Pikachu",
        type=["Electric"],
        level=22
    )

def create_mock_charmander() -> Pokemon:
    return Pokemon(
        id=4,
        name="Charmander",
        type=["Fire"],
        level=18
    )

def create_mock_squirtle() -> Pokemon:
    return Pokemon(
        id=7,
        name="Squirtle",
        type=["Water"],
        level=15
    )

def create_mock_bulbasaur() -> Pokemon:
    return Pokemon(
        id=10,
        name="Bulbasaur",
        type=["Grass", "Poison"],
        level=20
    )

def create_mock_jigglypuff() -> Pokemon:
    return Pokemon(
        id=25,
        name="Jigglypuff",
        type=["Normal", "Fairy"],
        level=14
    )

def create_mock_meowth() -> Pokemon:
    return Pokemon(
        id=39,
        name="Meowth",
        type=["Normal"],
        level=12
    )

