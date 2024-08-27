import { Pokemon } from "./pokemon.model";

function createPokedex() {
  function addPokemon(pokemon: Pokemon): void {
    // Implementation goes here
  }
  function getPokemonDetails(id: number): Pokemon | undefined {
    // Implementation goes here
    return undefined;
  }

  function removePokemon(id: number): void {
    // Implementation goes here
  }

  function getAllPokemon(): Pokemon[] {
    // Implementation goes here
    return [];
  }

  function searchPokemon(query: string): Pokemon[] {
    // Implementation goes here
    return [];
  }

  return {
    addPokemon,
    removePokemon,
    getPokemonDetails,
    getAllPokemon,
    searchPokemon,
  };
}
