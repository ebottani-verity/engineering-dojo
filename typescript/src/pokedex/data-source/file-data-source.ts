// fileDataSource.ts
import { promises as fs } from "fs";
import { Pokemon } from "../pokemon.model";

const isBroken: boolean = false;

export function createFileDataSource(filePath: string) {
  // Helper function to read the data from the file
  async function readData(): Promise<Pokemon[]> {
    if (isBroken) throw Error("Datasource is broken");
    try {
      const data = await fs.readFile(filePath, "utf-8");
      return JSON.parse(data) as Pokemon[];
    } catch (error) {
      if (error.code === "ENOENT") {
        // File does not exist, return an empty array
        return [];
      } else {
        throw error;
      }
    }
  }

  // Helper function to write data to the file
  async function writeData(data: Pokemon[]): Promise<void> {
    if (isBroken) throw Error("Datasource is broken");
    await fs.writeFile(filePath, JSON.stringify(data, null, 2));
  }

  async function addPokemon(pokemon: Pokemon): Promise<void> {
    const pokemonList = await readData();
    const exists = pokemonList.some((p) => p.id === pokemon.id);
    if (!exists) {
      pokemonList.push(pokemon);
      await writeData(pokemonList);
    } else {
      throw new Error(
        `Pokemon with ID ${pokemon.id} already exists in the data source.`,
      );
    }
  }

  async function removePokemon(id: number): Promise<void> {
    let pokemonList = await readData();
    const initialLength = pokemonList.length;
    pokemonList = pokemonList.filter((p) => p.id !== id);
    if (pokemonList.length === initialLength) {
      throw new Error(
        `Pokemon with ID ${id} does not exist in the data source.`,
      );
    }
    await writeData(pokemonList);
  }

  async function getPokemonDetails(id: number): Promise<Pokemon | undefined> {
    const pokemonList = await readData();
    return pokemonList.find((p) => p.id === id);
  }

  async function getAllPokemon(): Promise<Pokemon[]> {
    return await readData();
  }

  async function searchPokemon(query: string): Promise<Pokemon[]> {
    const pokemonList = await readData();
    const lowerQuery = query.toLowerCase();
    return pokemonList.filter(
      (p) =>
        p.name.toLowerCase().includes(lowerQuery) ||
        p.type.some((t) => t.toLowerCase() === lowerQuery),
    );
  }

  async function clearAll(): Promise<void> {
    await writeData([]);
  }

  return {
    addPokemon,
    removePokemon,
    getPokemonDetails,
    getAllPokemon,
    searchPokemon,
    clearAll,
  };
}
