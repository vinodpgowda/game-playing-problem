# AI Agent for Red-Blue Nim

## Project Overview  

The AI Agent for Red-Blue Nim is designed to play a modified version of the Nim game against a human player. Using Minimax with Alpha-Beta Pruning, it calculates optimal moves to ensure strategic gameplay in both standard and misère versions of the game. The game involves two piles of marbles, and players take turns removing marbles. The outcome depends on the version played and the marbles left in the piles.

The game involves two piles of marbles: red and blue. Players take turns removing marbles from a pile, and the outcome depends on the version played and the marbles left.

### Game Variants:
- **Standard**: The player loses if a pile is empty on their turn.
- **Misère**: The player wins if a pile is empty on their turn.

## Key Features

- Implements **Minimax with Alpha-Beta Pruning** for efficient decision-making.
- Supports both **standard** and **misère** game variants.
- Computes scores based on remaining marbles (2 points per red marble, 3 points per blue marble).
- Interactive gameplay where human players provide inputs via the command line.

## Code Structure

The code is written in **Python** and follows a functional programming approach with a procedural flow for game execution.

### Key Functions:
1. **alpha_beta_decision(state)**: Determines the optimal move using Minimax with Alpha-Beta Pruning.
2. **max_value(state, alpha, beta)**: Calculates the maximum utility for the AI player.
3. **min_value(state, alpha, beta)**: Calculates the minimum utility for the opponent.
4. **terminal_test(state)**: Checks if the game has reached an end state.
5. **utility(state)**: Computes the score for a given state based on the marbles left.
6. **result(action, state)**: Updates the game state based on the chosen action.

## Running the Game

### Prerequisites
- **Python 3.9+**

### Command-Line Usage
Run the program using the following format:
```bash
python red_blue_nim.py <num-red> <num-blue> <first-player>
```

### Parameters

- `<num-red>`: Number of red marbles.
- `<num-blue>`: Number of blue marbles.
- `<first-player>` (optional): Set to `human` for the human to start. Defaults to the computer.

### Examples

- Start with 13 red marbles, 15 blue marbles, and the computer as the first player:
    ```bash
    python red_blue_nim.py 13 15
    ```

- Start with 21 red marbles, 19 blue marbles, and the human as the first player:
    ```bash
    python red_blue_nim.py 21 19 human
    ```

### Notes

- Ensure the number of red and blue marbles is specified. If not, the program will exit with an error.

### Repository Contents

- **Source Code**: `red_blue_nim.py`
- **Readme File**: `README.md`

### Future Scope

- Implement depth-limited Minimax for enhanced scalability.
- Add visualization to represent the state space and decision-making process.
- Extend the game to support multiplayer scenarios.

