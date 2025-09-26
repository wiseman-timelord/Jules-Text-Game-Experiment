import blessed

# Import the core components of the game
from map import Map, CHUNK_WIDTH, CHUNK_HEIGHT
from player import Player
from renderer import Renderer

def main():
    """
    Main game function where the primary loop runs.
    """
    term = blessed.Terminal()
    running = True
    map_view_active = False # State to track if the map screen is shown

    # Initialize game components
    world_map = Map()
    player = Player(start_x=CHUNK_WIDTH // 2, start_y=CHUNK_HEIGHT // 2)
    renderer = Renderer(term)

    # The first chunk must be generated for the game to start
    world_map.get_chunk(player.chunk_x, player.chunk_y)

    # Use blessed's context managers for a clean, fullscreen terminal interface
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while running:
            # Decide which view to draw based on the current state
            if map_view_active:
                renderer.draw_map_screen(player, world_map)
            else:
                renderer.draw(player, world_map)

            # Wait for and process user input
            key = term.inkey(timeout=0.1)

            # Handle movement and other actions
            if key == 'm':
                map_view_active = not map_view_active
            elif key == 'q':
                running = False
            elif key.is_sequence and not map_view_active: # Only allow movement in game view
                if key.code == term.KEY_UP:
                    player.move(0, -1, world_map)
                elif key.code == term.KEY_DOWN:
                    player.move(0, 1, world_map)
                elif key.code == term.KEY_LEFT:
                    player.move(-1, 0, world_map)
                elif key.code == term.KEY_RIGHT:
                    player.move(1, 0, world_map)

def start():
    """
    The entry point for the game, called by launcher.py.
    """
    print("Starting game...")
    try:
        main()
        print("Game exited normally.")
    except Exception as e:
        print(f"An error occurred during game execution: {e}")

if __name__ == "__main__":
    start()