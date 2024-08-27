import { Pokemon } from "./pokemon.model";

export function createMockPikachu(): Pokemon {
  return {
    id: 1,
    name: "Pikachu",
    type: ["Electric"],
    level: 22,
  };
}

export function createMockCharmander(): Pokemon {
  return {
    id: 4,
    name: "Charmander",
    type: ["Fire"],
    level: 18,
  };
}

export function createMockSquirtle(): Pokemon {
  return {
    id: 7,
    name: "Squirtle",
    type: ["Water"],
    level: 15,
  };
}

export function createMockBulbasaur(): Pokemon {
  return {
    id: 10,
    name: "Bulbasaur",
    type: ["Grass", "Poison"],
    level: 20,
  };
}

export function createMockJigglypuff(): Pokemon {
  return {
    id: 25,
    name: "Jigglypuff",
    type: ["Normal", "Fairy"],
    level: 14,
  };
}

export function createMockMeowth(): Pokemon {
  return {
    id: 39,
    name: "Meowth",
    type: ["Normal"],
    level: 12,
  };
}
