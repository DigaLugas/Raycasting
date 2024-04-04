# Raycasting in Python with Pygame

This is a simple implementation of raycasting using Pygame in Python.

## Overview

This program demonstrates raycasting, a technique used in computer graphics for simulating the effect of a 3D environment using 2D graphics. The program creates a simple maze-like environment and allows the user to navigate through it. Raycasting is used to determine the distances to walls and render the environment from the player's perspective.

## Requirements
- For Python:
    - Python 3.x
    - Pygame library
- For JavaScript(p5.js):
    - A modern web browser
## Installation
# Python(Pygame) 
1. Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install Pygame using pip:
```bash
pip install pygame
```


# JavaScript
1. Clone or download the repository to your local machine

2. Navigate to the directory containing the HTML file and the JavaScript files.



## Usage
# Python 
1. Clone or download the repository to your local machine.

2. Navigate to the directory containing the `main.py` file.

3. Run the script using Python:
```bash
python raycasting.py
```
4. Use the arrow keys to move the player and the left and right arrow keys to rotate the view.

# JavaScript
1. Open the HTML file (index.html) in a modern web browser.


## Code Explanation

- **draw_map**: This function is responsible for rendering the maze environment. It iterates over the map array and draws each tile on the screen using Pygame's `pygame.draw.rect()` function.

- **cast_rays**: This function performs raycasting to determine the distances to walls and render them. It iterates over a fixed number of rays and checks for intersections with walls in the maze. For each intersection, it calculates the distance to the wall and renders it on the screen.

- **Main Game Loop**: The main game loop handles user input, updates the player's position and angle based on key presses, and renders the scene. It listens for key presses to move the player forward, backward, or rotate left and right. It also updates the player's position accordingly and redraws the scene on each frame.

These components work together to create a simple raycasting engine that simulates a 3D environment using 2D graphics. The maze environment is rendered using raycasting techniques, allowing the player to navigate through it and explore the surroundings.

## Version 
- Python Raycasting (1.0.1β)

- JavaScript Raycasting (1.0.0 α)

## Credits

This program is inspired by the tutorial series on raycasting by [OneLoneCoder](https://www.youtube.com/c/javidx9).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
