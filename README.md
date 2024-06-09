# Snake Game

Welcome to the Snake Game! This is a classic snake game implemented using the Python `turtle` module. The objective is to control the snake to eat food, grow longer, and avoid collisions with the walls or its own tail.

## Prerequisites

- Python 3.x
- `turtle` module (standard with Python)

## Installation

1. Clone this repository or download the source code files.

    ```sh
    git clone https://github.com/yourusername/snake-game.git
    cd snake-game
    ```

2. Ensure you have the required background image file `snakebg.gif` in the same directory as the script.

## Files

- `main.py`: The main script to run the game.
- `snake.py`: Contains the `Snake` class which handles snake behavior.
- `food.py`: Contains the `Food` class which manages the food for the snake.
- `scoreboard.py`: Contains the `Scoreboard` class to track and display the score.

## How to Play

1. Run the game by executing the main script.

    ```sh
    python main.py
    ```

2. Control the snake using the arrow keys:
    - Up: Move up
    - Down: Move down
    - Left: Move left
    - Right: Move right

3. The objective is to eat the food (red dot). Each time the snake eats food, it grows longer, and your score increases.

4. Avoid colliding with the walls or the snake's own tail. The game ends if either of these collisions occurs.
