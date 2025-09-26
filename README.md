# Jules-Text-Game-Experiment
Status: Alpha

### Description:
This project is an experiment in creating a procedurally generating text adventure game. The goal is to build an infinitely explorable world rendered entirely with ASCII art. The player can roam freely, and new segments of the map are generated on the fly as they venture into unknown territory. The current version establishes the core engine and basic gameplay mechanics.

### Features:
- **Procedurally Generated World:** The game world is composed of individual map "chunks" that are generated as the player enters them, creating a unique and near-infinite landscape to explore, currently populated with simple rocks and bushes.
- **Player Exploration:** Navigate the world using the arrow keys. The game remembers previously visited areas.
- **Dynamic Map Screen:** Toggle a high-level map view with the 'm' key to see which parts of the world you have discovered.
- **Planned Biomes:** The architecture is designed to support different environments, with plans for Urban, Outlands, and Wasteland biomes.
- **Standalone Installation:** Includes simple installer and validator scripts to set up the environment and dependencies.

### Preview
- We now have mostly done the, batch, bash, installer, here is the installer currently...
```
===============================================================================
    Jules' Text Adventure Game - Installation
===============================================================================

Managing 'data\settings.json'...
Replaced 'data\settings.json'.
Cleaning up old virtual environment ('.venv')...
Removed existing '.venv' directory.
Creating new virtual environment...
.venv directory Created... OK

Upgrading pip to latest version...
Requirement already satisfied: pip in c:\game_files\jules-text-game-experiment\j
ules-text-game-experiment-feature-initial-game-setup 004\jules-text-game-experim
ent-feature-initial-game-setup\.venv\lib\site-packages (24.0)
Collecting pip
  Using cached pip-25.2-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-25.2-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-25.2

Installing requirements...
Collecting blessed
  Using cached blessed-1.22.0-py2.py3-none-any.whl.metadata (13 kB)
Collecting perlin-noise
  Using cached perlin_noise-1.14-py3-none-any.whl.metadata (472 bytes)
Collecting wcwidth>=0.1.4 (from blessed)
  Using cached wcwidth-0.2.14-py2.py3-none-any.whl.metadata (15 kB)
Collecting jinxed>=1.1.0 (from blessed)
  Using cached jinxed-1.3.0-py2.py3-none-any.whl.metadata (4.7 kB)
Collecting ansicon (from jinxed>=1.1.0->blessed)
  Using cached ansicon-1.89.0-py2.py3-none-any.whl.metadata (2.8 kB)
Using cached blessed-1.22.0-py2.py3-none-any.whl (85 kB)
Using cached perlin_noise-1.14-py3-none-any.whl (4.6 kB)
Using cached jinxed-1.3.0-py2.py3-none-any.whl (33 kB)
Using cached wcwidth-0.2.14-py2.py3-none-any.whl (37 kB)
Using cached ansicon-1.89.0-py2.py3-none-any.whl (63 kB)
Installing collected packages: ansicon, wcwidth, perlin-noise, jinxed, blessed
Successfully installed ansicon-1.89.0 blessed-1.22.0 jinxed-1.3.0 perlin-noise-1
.14 wcwidth-0.2.14

--- Installation Report ---
All steps completed successfully!
Virtual environment created at: C:\Game_Files\Jules-Text-Game-Experiment\Jules-T
ext-Game-Experiment-feature-initial-game-setup 004\Jules-Text-Game-Experiment-fe
ature-initial-game-setup\.venv
Required packages installed: blessed, perlin-noise
You can now run the game using option 1 from the main menu.
-----------------------------------------------------------

-------------------------------------------------------------------------------

"Installation process complete. Press any key to return to the menu."
```


## Gamekeys listed...
```
k = keys
m = map
r = restart
q = quit
```

## Notation:
- There is also new "OK Computer" by `Kimi.Com`, I'd like to see what it would do also.
- Jules updates  to a new branch, main is updated manually from the Jules branch.
