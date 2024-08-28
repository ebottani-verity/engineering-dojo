from typing import List, Optional

from src.pokedex.pokemon import Pokemon

class PokemonDataSource:
    def __init__(self):
        # Private list to store the Pokemon objects
        self._pokemon_list: List[Pokemon] = []

    # Add a new Pokemon to the data source
    def add_pokemon(self, pokemon: Pokemon) -> None:
        exists = any(p.id == pokemon.id for p in self._pokemon_list)
        if not exists:
            self._pokemon_list.append(pokemon)
        else:
            raise ValueError(f"Pokemon with ID {pokemon.id} already exists in the data source.")

    # Remove a Pokemon from the data source by ID
    def remove_pokemon(self, id: int) -> None:
        initial_length = len(self._pokemon_list)
        self._pokemon_list = [p for p in self._pokemon_list if p.id != id]
        if len(self._pokemon_list) == initial_length:
            raise ValueError(f"Pokemon with ID {id} does not exist in the data source.")

    # Retrieve details of a specific Pokemon by ID
    def get_pokemon_details(self, id: int) -> Optional[Pokemon]:
        return next((p for p in self._pokemon_list if p.id == id), None)

    # List all Pokemon in the data source
    def get_all_pokemon(self) -> List[Pokemon]:
        return self._pokemon_list.copy()  # Return a copy to prevent external mutations

    # Search for Pokemon by name or type
    def search_pokemon(self, query: str) -> List[Pokemon]:
        lower_query = query.lower()
        return [
            p for p in self._pokemon_list
            if lower_query in p.name.lower() or any(lower_query in t.lower() for t in p.type)
        ]

    # Clear all Pokemon from the data source (for testing or resetting purposes)
    def clear_all(self) -> None:
        self._pokemon_list = []
