# Define a Pokemon dictionary structure
from typing import List, Dict, Optional

# Initialize an empty list to store the Pokemon list
pokemon_list: List[Dict[str, any]] = []

# Function to add a new Pokemon to the Pokedex
def add_pokemon(pokemon: Dict[str, any]) -> None:
    # Implementation goes here
    pass

# Function to remove a Pokemon from the Pokedex by ID
def remove_pokemon(pokemon_id: int) -> None:
    # Implementation goes here
    pass

# Function to retrieve details of a specific Pokemon by ID
def get_pokemon_details(pokemon_id: int) -> Optional[Dict[str, any]]:
    # Implementation goes here
    pass

# Function to list all Pokemon in the Pokedex
def get_all_pokemon() -> List[Dict[str, any]]:
    # Implementation goes here
    pass

# Function to search for Pokemon by name or type
def search_pokemon(query: str) -> List[Dict[str, any]]:
    # Implementation goes here
    pass