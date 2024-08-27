import { ModifiedPokemon } from "../pokemon.model";

export function createDisplay() {
  function logAddPokemon(pokemon: ModifiedPokemon): void {
    console.log(`Pokemon ${pokemon.name} has been added to the Pokedex.`);
    logModifiers(pokemon);
  }

  function logRemovePokemon(pokemon: ModifiedPokemon): void {
    console.log(`Pokemon ${pokemon.name} has been removed from the Pokedex.`);
  }

  function logGetPokemonDetails(pokemon: ModifiedPokemon): void {
    console.log(`Details retrieved for Pokemon ${pokemon.name}.`);
    logModifiers(pokemon);
  }

  function logSearchPokemon(query: string, results: ModifiedPokemon[]): void {
    console.log(`Search for "${query}" returned ${results.length} result(s).`);
    results.forEach((pokemon) => logModifiers(pokemon));
  }

  function logGetAllPokemon(pokemons: ModifiedPokemon[]): void {
    console.log(`Retrieved all Pokemon. Total count: ${pokemons.length}.`);
    pokemons.forEach((pokemon) => logModifiers(pokemon));
  }

  function logModifiers(pokemon: ModifiedPokemon): void {
    const { attackModifier, defenseModifier, speedModifier } =
      pokemon.modifiers;
    console.log(
      `Modifiers for ${pokemon.name}: Attack: ${attackModifier.toFixed(2)}, Defense: ${defenseModifier.toFixed(2)}, Speed: ${speedModifier.toFixed(2)}`,
    );
  }

  return {
    logAddPokemon,
    logRemovePokemon,
    logGetPokemonDetails,
    logSearchPokemon,
    logGetAllPokemon,
    logModifiers,
  };
}
