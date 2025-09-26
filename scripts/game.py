import blessed

# Import the core components of the game
from map import Map, CHUNK_WIDTH, CHUNK_HEIGHT
from player import Player
from renderer import Renderer

def initialize_game_state():
    """Creates and returns a new set of game state objects for a new game."""
    world_map = Map()
    player = Player(start_x=CHUNK_WIDTH // 2, start_y=CHUNK_HEIGHT // 2)
    # The first chunk must be generated for the game to start
    world_map.get_chunk(player.chunk_x, player.chunk_y)
    return world_map, player

def main():
    """
    Main game function where the primary loop runs.
    """
    term = blessed.Terminal()
    running = True
    map_view_active = False
    keys_view_active = False

    # Initialize game components
    world_map, player = initialize_game_state()
    renderer = Renderer(term)

    # Use blessed's context managers for a clean, fullscreen terminal interface
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while running:
            # Decide which view to draw based on the current state.
            # The keys screen takes precedence over the map screen.
            if keys_view_active:
                renderer.draw_keys_screen()
            elif map_view_active:
                renderer.draw_map_screen(player, world_map)
            else:
                renderer.draw(player, world_map)

            # Wait for and process user input
            key = term.inkey(timeout=0.1)

            # A view is active if either the map or keys screen is shown.
            a_view_is_active = map_view_active or keys_view_active

            # Handle global keys first
            if key == 'k':
                keys_view_active = not keys_view_active
                # Ensure map view is off when keys view is activated
                if keys_view_active:
                    map_view_active = False
            elif key == 'q':
                running = False
            elif key == 'r':
                world_map, player = initialize_game_state()
                map_view_active = False
                keys_view_active = False
            elif key == 'm':
                map_view_active = not map_view_active
                # Ensure keys view is off when map view is activated
                if map_view_active:
                    keys_view_active = False

            # Handle player movement only if no other view is active
            elif key.is_sequence and not a_view_is_active:
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