# Exercise: Building a Simple Pokedex
**Objective**: Pairing teams will develop a simple Pokedex feature, with a focus on writing unit, focus on reviewing these learning
- Red green refactor
- Golden rule of TDD
- Test as design tool
- Command query separation
- Qualities of a good unit test
- Three style of unit test

## Exercise Setup:
**Language/Framework**: Use a familiar programming language and testing framework (e.g., JavaScript with Jest, Python with pytest, Java with JUnit). 

**Timeframe**: Allocate around 2-3 hours for this exercise.

**Initial Codebase**: Start with a basic scaffold of the Pokedex, such as a class with methods like addPokemon, removePokemon, getPokemonDetails, and getAllPokemon.

# Step-by-Step Exercise Plan:
## Understand the Requirements:

- Feature 1: Add a Pokémon to the Pokedex.
- Feature 2: Retrieve details of a specific Pokémon.
- Feature 3: List all Pokémon in the Pokedex.
- Feature 4: Remove a Pokémon from the Pokedex.
- Feature 5: Search for Pokémon by type or name.

# Acceptance Criteria
- Leverage the provided data-source to persist your pokemons
- Every action on the system needs to be displayed using the display component 
- Getting pokemon details, and listing all pokemon requires modifiers to be displayed

## Define Unit Tests Together:
Discuss which type of test you want to write
- state based
- output based
- communication based

Discuss and define test cases before writing any code. Ensure that each test is designed to:
- Protect against regressions: For example, after adding a Pokémon to the Pokedex, ensure that it can be retrieved and that removing it actually deletes the correct entry.
- Resist refactoring: Avoid tying tests to specific implementation details (e.g., the internal storage structure) and instead focus on the behavior (e.g., the Pokedex should always return accurate Pokémon details regardless of how they’re stored internally).
- Provide fast feedback: Keep the tests simple and efficient, ensuring they run quickly even as the Pokedex grows with more Pokémon.
- Be maintainable: Write tests that are clear and concise, using descriptive names and avoiding duplication, so they are easy to update when the Pokedex features evolve.

Try to develop at least two tests that maximises the first and the second point. Reflect on how you can make sure to maximise the last point in each of these tests. 
Hint: What is your unit?






















# PART 2
Now switch your data source to use the file-data-source
# PART 3 
Open the file data source and turn the switch on, what happens to your tests? 












