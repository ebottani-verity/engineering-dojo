from typing import List

class Pokemon:
    def __init__(self, id: int, name: str, type: List[str], level: int):
        self.id = id
        self.name = name
        self.type = type
        self.level = level
