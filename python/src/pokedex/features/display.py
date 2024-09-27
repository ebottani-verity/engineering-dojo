from src.pokedex.pokemon import ModifiedPokemon, Pokemon


class PokemonDisplay:
    def log_add_pokemon(self, pokemon: Pokemon) -> None:
        print(f"Pokemon {pokemon.name} has been added to the Pokedex.")

    def log_remove_pokemon(self, pokemon: ModifiedPokemon) -> None:
        print(f"Pokemon {pokemon.name} has been removed from the Pokedex.")

    def log_get_pokemon_details(self, pokemon: ModifiedPokemon) -> None:
        print(f"Details retrieved for Pokemon {pokemon.name}.")
        self.log_modifiers(pokemon)

    def log_search_pokemon(self, query: str, results: list) -> None:
        print(f'Search for "{query}" returned {len(results)} result(s).')
        for pokemon in results:
            print(f"Pokemon {pokemon.name} has been found in Pokedex.")

    def log_get_all_pokemon(self, pokemons: list) -> None:
        print(f"Retrieved all Pokemon. Total count: {len(pokemons)}.")
        for pokemon in pokemons:
            self.log_modifiers(pokemon)

    def log_modifiers(self, pokemon: ModifiedPokemon) -> None:
        attack_modifier = pokemon.modifiers.get("attackModifier", 1)
        defense_modifier = pokemon.modifiers.get("defenseModifier", 1)
        speed_modifier = pokemon.modifiers.get("speedModifier", 1)
        print(
            f"Modifiers for {pokemon.name}: "
            f"Attack: {attack_modifier:.2f}, "
            f"Defense: {defense_modifier:.2f}, "
            f"Speed: {speed_modifier:.2f}"
        )