import { Modifiers, Pokemon } from "./pokemon.model";

export function createModifierCalculator() {
  function calculateModifiers(pokemon: Pokemon): Modifiers {
    let attackModifier = 1;
    let defenseModifier = 1;
    let speedModifier = 1;

    // Example logic for buffs and nerfs based on type and level
    // Buffs: Increase stats if level is above 20
    if (pokemon.level > 20) {
      attackModifier += 0.2; // +20% attack
      defenseModifier += 0.2; // +20% defense
      speedModifier += 0.2; // +20% speed
    }

    // Nerfs: Decrease stats if level is below 10
    if (pokemon.level < 10) {
      attackModifier -= 0.1; // -10% attack
      defenseModifier -= 0.1; // -10% defense
      speedModifier -= 0.1; // -10% speed
    }

    // Type-based buffs/nerfs
    if (pokemon.type.includes("Fire")) {
      attackModifier += 0.1; // +10% attack for Fire types
    }

    if (pokemon.type.includes("Water")) {
      defenseModifier += 0.1; // +10% defense for Water types
    }

    if (pokemon.type.includes("Electric")) {
      speedModifier += 0.1; // +10% speed for Electric types
    }

    // Example of a nerf: Grass type might have a defense nerf
    if (pokemon.type.includes("Grass")) {
      defenseModifier -= 0.1; // -10% defense for Grass types
    }

    return {
      attackModifier,
      defenseModifier,
      speedModifier,
    };
  }

  return {
    calculateModifiers,
  };
}
