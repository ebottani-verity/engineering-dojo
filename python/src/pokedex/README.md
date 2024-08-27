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

## Define Unit Tests Together:
Discuss and define test cases before writing any code. Ensure that each test is designed to:
- Protect against regressions: For example, after adding a Pokémon to the Pokedex, ensure that it can be retrieved and that removing it actually deletes the correct entry.
- Resist refactoring: Avoid tying tests to specific implementation details (e.g., the internal storage structure) and instead focus on the behavior (e.g., the Pokedex should always return accurate Pokémon details regardless of how they’re stored internally).
- Provide fast feedback: Keep the tests simple and efficient, ensuring they run quickly even as the Pokedex grows with more Pokémon.
- Be maintainable: Write tests that are clear and concise, using descriptive names and avoiding duplication, so they are easy to update when the Pokedex features evolve.
Pair Programming: Implement Features with Tests:

Emphasize constant communication, with the developer writing tests explaining the rationale behind each test case, while the other ensures the code meets these expectations.

## Refactor the Code:
Introduce refactorings to the codebase, such as changing how Pokémon are stored (e.g., from a list to a dictionary/map) or restructuring the Pokedex class.
Ensure that tests still pass without modification, reinforcing the principle of Resistance to refactoring.
## Expand the Test Suite:
After implementing and testing all features, introduce edge cases or additional scenarios (e.g., handling duplicate Pokémon names, searching for non-existent Pokémon).
Ensure these tests are added in a way that maintains the speed and maintainability of the test suite.
## Review and Reflect:
Conduct a review session where each pair discusses:
- How well their tests protected against regressions.
- Whether their tests survived code refactoring without changes.
- If the tests provided fast feedback during development.
- How maintainable the tests are (e.g., were they easy to extend or modify?).

Consider what improvements could be made in the future to better adhere to the four pillars.
# Outcome:
By the end of the exercise, participants will have a deeper understanding of how to design and implement unit tests that are robust, reliable, and maintainable, specifically in the context of a Pokedex. This exercise will help solidify the importance of test-driven development (TDD) and the impact of good unit testing practices on code quality and development efficiency.

This Pokedex-themed exercise is a fun and engaging way to reinforce key testing concepts while working on something that’s both familiar and enjoyable for many developers.