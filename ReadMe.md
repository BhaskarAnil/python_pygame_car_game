# Car Game Using Pygame

Welcome to the Car Game built with Python and Pygame! This is a simple arcade-style game where you control a car, avoid oncoming vehicles, and try to achieve the highest score possible.

## Features

- Smooth car movement with keyboard controls

- Jump mechanic to avoid collisions

- Increasing difficulty as your score rises

- Background music and sound effects

## Requirements

- Python 3.7 or higher

- Pygame library

- All required Python packages are listed in requirements.txt.
  
## Installation

1. Clone the repository:

```
git clone git@gitlab.com:jeenubhaskaranil-group/python_pygame_car_game.git
cd python_pygame_car_game
```

2. Install dependencies:

```
pip install -r requirements.txt
```

Ensure the following directory structure:

```

python_pygame_car_game/
├── background_sound/
│   └── car_moving.mp3
├── elements_images/
│   ├── line.png
│   ├── oppvehicle2.png
│   ├── player_jump.png
│   └── player.png
├── main.py
├── requirements.txt
└── ReadMe.md

```

## How to Play

### Run the game:

```bash
python main.py
```

### Controls:

 - Start Game: Press the Up Arrow (↑)

 - Move Left: Press the Left Arrow (←)

 - Move Right: Press the Right Arrow (→)

 - Move Forward: Press the Up Arrow (↑)

 - Move Backward: Press the Down Arrow (↓)

 - Jump: Press the Space Bar (temporarily avoids collision)

### Objective:

 - Avoid oncoming vehicles for as long as possible.

 - Your score increases with time survived.

 - The game ends if you collide with another vehicle or go off the road.

### Restart:

 - After a game over, press the Up Arrow (↑) to play again.

### Troubleshooting
 - No sound/music: Ensure your system audio is not muted and that pygame.mixer is properly initialized.

 - Missing images/sounds: Double-check the folder structure and file names.

 - Pygame errors: Make sure Pygame is installed (pip install pygame) and you are using a compatible Python version.