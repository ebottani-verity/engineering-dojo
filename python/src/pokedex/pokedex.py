from typing import List, Dict, Optional
from src.pokedex.modified_pokemon import ModifiedPokemon
from src.pokedex.pokemon import Pokemon


class Pokedex:
    def __init__(self):
        self.pokemon_list: List[Dict[str, any]] = []

    # Function to add a new Pokemon to the Pokedex
    def add_pokemon(self, pokemon: Pokemon) -> None:
        pass

    # Function to remove a Pokemon from the Pokedex by ID
    def remove_pokemon(self, pokemon_id: int) -> None:
        # Implementation goes here
        pass

    # Function to retrieve details of a specific Pokemon by ID
    def get_pokemon_details(self, pokemon_id: int) -> ModifiedPokemon:
        pass


    # Function to list all Pokemon in the Pokedex
    def get_all_pokemon(self) -> List[Pokemon]:
        # Implementation goes here
        return self.data_source.get_all_pokemon()

    # Function to search for Pokemon by name or type
    def search_pokemon(self, query: str) -> List[Dict[str, any]]:
        # Implementation goes here
        pass