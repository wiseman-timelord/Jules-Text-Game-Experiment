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
- The installer currently...
```
--- Running Full Installation and Setup ---
1. Managing 'data\settings.json'...
  - Removed existing 'data\settings.json'.
  - Created clean 'data\settings.json'.
----------------------------------------
2. Cleaning up old virtual environment ('.venv')...
  - No existing '.venv' directory found. Skipping.
----------------------------------------
3. Creating new virtual environment...
  - Creating .venv directory... OK
----------------------------------------
4. Upgrading pip...
  - Upgrading pip to the latest version... OK
----------------------------------------
5. Installing required packages...
  - Installing blessed, perlin-noise... OK
----------------------------------------

--- Installation Report ---
All steps completed successfully!
Virtual environment created at: C:\Game_Files\Jules-Text-Game-Experiment\Jules-T
ext-Game-Experiment-feature-initial-game-setup 003\Jules-Text-Game-Experiment-fe
ature-initial-game-setup\.venv
Required packages installed: blessed, perlin-noise
You can now run the game using option 1 from the main menu.
---------------------------


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
