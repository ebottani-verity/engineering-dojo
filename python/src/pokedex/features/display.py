from src.pokedex.pokemon import ModifiedPokemon

def create_display():
    def log_add_pokemon(pokemon: ModifiedPokemon) -> None:
        print(f"Pokemon {pokemon.name} has been added to the Pokedex.")
        log_modifiers(pokemon)

    def log_remove_pokemon(pokemon: ModifiedPokemon) -> None:
        print(f"Pokemon {pokemon.name} has been removed from the Pokedex.")

    def log_get_pokemon_details(pokemon: ModifiedPokemon) -> None:
        print(f"Details retrieved for Pokemon {pokemon.name}.")
        log_modifiers(pokemon)

    def log_search_pokemon(query: str, results: list) -> None:
        print(f'Search for "{query}" returned {len(results)} result(s).')
        for pokemon in results:
            log_modifiers(pokemon)

    def log_get_all_pokemon(pokemons: list) -> None:
        print(f"Retrieved all Pokemon. Total count: {len(pokemons)}.")
        for pokemon in pokemons:
            log_modifiers(pokemon)

    def log_modifiers(pokemon: ModifiedPokemon) -> None:
        attack_modifier = pokemon.modifiers.get("attackModifier", 1)
        defense_modifier = pokemon.modifiers.get("defenseModifier", 1)
        speed_modifier = pokemon.modifiers.get("speedModifier", 1)
        print(
            f"Modifiers for {pokemon.name}: "
            f"Attack: {attack_modifier:.2f}, "
            f"Defense: {defense_modifier:.2f}, "
            f"Speed: {speed_modifier:.2f}"
        )

    return {
        "log_add_pokemon": log_add_pokemon,
        "log_remove_pokemon": log_remove_pokemon,
        "log_get_pokemon_details": log_get_pokemon_details,
        "log_search_pokemon": log_search_pokemon,
        "log_get_all_pokemon": log_get_all_pokemon,
        "log_modifiers": log_modifiers,
    }