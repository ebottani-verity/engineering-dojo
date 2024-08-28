import json
from typing import List, Optional
import os

from src.pokedex.pokemon import Pokemon

# Global flag to simulate a broken data source
is_broken: bool = False

def create_file_data_source(file_path: str):
    # Helper function to read the data from the file
    def read_data() -> List[Pokemon]:
        if is_broken:
            raise Exception("Datasource is broken")
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return [Pokemon(**item) for item in data]
        except FileNotFoundError:
            # File does not exist, return an empty array
            return []
        except Exception as error:
            raise error

    # Helper function to write data to the file
    def write_data(data: List[Pokemon]) -> None:
        if is_broken:
            raise Exception("Datasource is broken")
        with open(file_path, 'w') as file:
            json.dump([pokemon.__dict__ for pokemon in data], file, indent=2)

    def add_pokemon(pokemon: Pokemon) -> None:
        pokemon_list = read_data()
        exists = any(p.id == pokemon.id for p in pokemon_list)
        if not exists:
            pokemon_list.append(pokemon)
            write_data(pokemon_list)
        else:
            raise ValueError(f"Pokemon with ID {pokemon.id} already exists in the data source.")

    def remove_pokemon(id: int) -> None:
        pokemon_list = read_data()
        initial_length = len(pokemon_list)
        pokemon_list = [p for p in pokemon_list if p.id != id]
        if len(pokemon_list) == initial_length:
            raise ValueError(f"Pokemon with ID {id} does not exist in the data source.")
        write_data(pokemon_list)

    def get_pokemon_details(id: int) -> Optional[Pokemon]:
        pokemon_list = read_data()
        return next((p for p in pokemon_list if p.id == id), None)

    def get_all_pokemon() -> List[Pokemon]:
        return read_data()

    def search_pokemon(query: str) -> List[Pokemon]:
        pokemon_list = read_data()
        lower_query = query.lower()
        return [
            p for p in pokemon_list
            if lower_query in p.name.lower() or any(lower_query in t.lower() for t in p.type)
        ]

    def clear_all() -> None:
        write_data([])

    return {
        'add_pokemon': add_pokemon,
        'remove_pokemon': remove_pokemon,
        'get_pokemon_details': get_pokemon_details,
        'get_all_pokemon': get_all_pokemon,
        'search_pokemon': search_pokemon,
        'clear_all': clear_all,
    }
