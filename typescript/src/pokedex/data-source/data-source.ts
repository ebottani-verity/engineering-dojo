// dataSource.ts
import { Pokemon } from "../pokedex"; // Import the Pokemon interface from the Pokedex module

export function createDataSource() {
  // Private array to store the list of Pokemon
  let pokemonList: Pokemon[] = [];

  // Add a new Pokemon to the data source
  function addPokemon(pokemon: Pokemon): void {
    const exists = pokemonList.some((p) => p.id === pokemon.id);
    if (!exists) {
      pokemonList.push(pokemon);
    } else {
      throw new Error(
        `Pokemon with ID ${pokemon.id} already exists in the data source.`,
      );
    }
  }

  // Remove a Pokemon from the data source by ID
  function removePokemon(id: number): void {
    const initialLength = pokemonList.length;
    pokemonList = pokemonList.filter((p) => p.id !== id);
    if (pokemonList.length === initialLength) {
      throw new Error(
        `Pokemon with ID ${id} does not exist in the data source.`,
      );
    }
  }

  // Retrieve details of a specific Pokemon by ID
  function getPokemonDetails(id: number): Pokemon | undefined {
    return pokemonList.find((p) => p.id === id);
  }

  // List all Pokemon in the data source
  function getAllPokemon(): Pokemon[] {
    return [...pokemonList]; // Return a copy to prevent external mutations
  }

  // Search for Pokemon by name or type
  function searchPokemon(query: string): Pokemon[] {
    const lowerQuery = query.toLowerCase();
    return pokemonList.filter(
      (p) =>
        p.name.toLowerCase().includes(lowerQuery) ||
        p.type.some((t) => t.toLowerCase() === lowerQuery),
    );
  }

  // Clear all Pokemon from the data source (for testing or resetting purposes)
  function clearAll(): void {
    pokemonList = [];
  }

  // Return an object containing all the data source methods
  return {
    addPokemon,
    removePokemon,
    getPokemonDetails,
    getAllPokemon,
    searchPokemon,
    clearAll,
  };
}
