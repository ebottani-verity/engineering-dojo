from src.pokedex.pokemon import Pokemon
from src.pokedex.utils.modifier_calculator import Modifiers


class ModifiedPokemon:
    def __init__(self, pokemon: Pokemon, modifiers: Modifiers):
        self.id = pokemon.id
        self.name = pokemon.name
        self.type = pokemon.type
        self.level = pokemon.level
        self.modifiers = modifiers