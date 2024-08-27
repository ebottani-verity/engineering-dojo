// Pokemon interface representing the structure of a Pokemon object
export interface Pokemon {
  id: number;
  name: string;
  type: string[];
  level: number;
}

export type Modifiers = {
  attackModifier: number;
  defenseModifier: number;
  speedModifier: number;
};

export interface ModifiedPokemon extends Pokemon {
  modifiers: Modifiers;
}
