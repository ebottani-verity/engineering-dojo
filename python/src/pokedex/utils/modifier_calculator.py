from typing import Dict, List

from src.pokedex.pokemon import Pokemon


class ModifierCalculator:
    @staticmethod
    def calculate_modifiers(pokemon: Pokemon) -> Dict[str, float]:
        attack_modifier = 1.0
        defense_modifier = 1.0
        speed_modifier = 1.0

        # Example logic for buffs and nerfs based on type and level
        # Buffs: Increase stats if level is above 20
        if pokemon.level > 20:
            attack_modifier += 0.2  # +20% attack
            defense_modifier += 0.2  # +20% defense
            speed_modifier += 0.2  # +20% speed

        # Nerfs: Decrease stats if level is below 10
        if pokemon.level < 10:
            attack_modifier -= 0.1  # -10% attack
            defense_modifier -= 0.1  # -10% defense
            speed_modifier -= 0.1  # -10% speed

        # Type-based buffs/nerfs
        if "Fire" in pokemon.type:
            attack_modifier += 0.1  # +10% attack for Fire types

        if "Water" in pokemon.type:
            defense_modifier += 0.1  # +10% defense for Water types

        if "Electric" in pokemon.type:
            speed_modifier += 0.1  # +10% speed for Electric types

        # Example of a nerf: Grass type might have a defense nerf
        if "Grass" in pokemon.type:
            defense_modifier -= 0.1  # -10% defense for Grass types

        return {
            "attackModifier": attack_modifier,
            "defenseModifier": defense_modifier,
            "speedModifier": speed_modifier,
        }

