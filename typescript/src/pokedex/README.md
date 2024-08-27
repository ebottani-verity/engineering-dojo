# Exercise: Building a Simple Pokedex
**Objective**: Pairing teams will develop a simple Pokedex feature, with a focus on writing unit tests that adhere to the four pillars of good unit tests: 
- Protection against regressions, 
- Resistance to refactoring, 
- Fast feedback, 
- and Maintainability.

## Exercise Setup:
**Language/Framework**: Use a familiar programming language and testing framework (e.g., JavaScript with Jest, Python with pytest, Java with JUnit). 

**Timeframe**: Allocate around 2-3 hours for this exercise.

**Initial Codebase**: Start with a basic scaffold of the Pokedex, such as a class with methods like addPokemon, removePokemon, getPokemonDetails, and getAllPokemon.

# Step-by-Step Exercise Plan:
## Understand the Requirements:

- Feature 1: Add a Pokémon to the Pokedex.
- Feature 2: Remove a Pokémon from the Pokedex.
- Feature 3: Retrieve details of a specific Pokémon.
- Feature 4: List all Pokémon in the Pokedex.
- Feature 5: Search for Pokémon by type or name.

# Acceptance Criteria
- Leverage the provided data-source to persist your pokemons
- A pokemon can be visualised only when modifiers have been applied
- Every action on the system needs to be displayed using the display component 

## Define Unit Tests Together:
Discuss and define test cases before writing any code. Ensure that each test is designed to:
- Protect against regressions: For example, after adding a Pokémon to the Pokedex, ensure that it can be retrieved and that removing it actually deletes the correct entry.
- Resist refactoring: Avoid tying tests to specific implementation details (e.g., the internal storage structure) and instead focus on the behavior (e.g., the Pokedex should always return accurate Pokémon details regardless of how they’re stored internally).
- Provide fast feedback: Keep the tests simple and efficient, ensuring they run quickly even as the Pokedex grows with more Pokémon.
- Be maintainable: Write tests that are clear and concise, using descriptive names and avoiding duplication, so they are easy to update when the Pokedex features evolve.

Try to develop at two test that maximises the first and the second point. Reflect on how you can make sure to maximise the last point in each of these tests. 
Hint: What is your unit?