# We need to import the map constants to understand chunk dimensions and wall tiles.
from map import CHUNK_WIDTH, CHUNK_HEIGHT
from ascii_art import PLAYER, WALL

class Player:
    """
    Manages the player's state, including position and movement.
    """

    def __init__(self, start_x, start_y, start_chunk_x=0, start_chunk_y=0):
        """
        Initializes the player at a specific position.

        Args:
            start_x (int): The starting x-coordinate within the chunk.
            start_y (int): The starting y-coordinate within the chunk.
            start_chunk_x (int): The starting chunk's x-coordinate.
            start_chunk_y (int): The starting chunk's y-coordinate.
        """
        self.x = start_x
        self.y = start_y
        self.chunk_x = start_chunk_x
        self.chunk_y = start_chunk_y
        self.symbol = PLAYER

    def move(self, dx, dy, world_map):
        """
        Handles player movement and chunk transitions.

        Args:
            dx (int): The change in the x-direction (-1, 0, or 1).
            dy (int): The change in the y-direction (-1, 0, or 1).
            world_map (Map): The world map object, used for collision detection.
        """
        # Calculate the potential new coordinates.
        new_x = self.x + dx
        new_y = self.y + dy

        # Check for chunk transitions first.
        # This ensures the player wraps to a new chunk before checking for
        # collisions in the current one.
        if new_x < 0:
            self.chunk_x -= 1
            self.x = CHUNK_WIDTH - 2  # Appear on the right side of the new chunk
            return
        elif new_x >= CHUNK_WIDTH:
            self.chunk_x += 1
            self.x = 1  # Appear on the left side of the new chunk
            return

        if new_y < 0:
            self.chunk_y -= 1
            self.y = CHUNK_HEIGHT - 2  # Appear on the bottom side
            return
        elif new_y >= CHUNK_HEIGHT:
            self.chunk_y += 1
            self.y = 1  # Appear on the top side
            return

        # If not transitioning, check for collisions within the current chunk.
        # Get the current chunk data from the world map.
        current_chunk_data = world_map.get_chunk(self.chunk_x, self.chunk_y)

        # Check if the destination tile is a wall.
        if current_chunk_data[new_y][new_x] != WALL:
            # If it's not a wall, update the player's position.
            self.x = new_x
            self.y = new_y

# This block allows for testing the player movement logic independently.
if __name__ == '__main__':
    from map import Map

    print("--- Testing Player Movement ---")

    # Setup a mock world and a player.
    test_map = Map()
    player = Player(start_x=5, start_y=5)

    print(f"Initial Position: Chunk({player.chunk_x}, {player.chunk_y}), Coords({player.x}, {player.y})")

    # --- Test 1: Simple movement ---
    player.move(1, 0, test_map)
    print(f"Moved right. New Position: Coords({player.x}, {player.y})")
    assert player.x == 6 and player.y == 5

    # --- Test 2: Collision with a wall ---
    # The player is at (6, 5). We will place a wall at (7, 5) to block the next move.
    test_map.get_chunk(0, 0)[5][7] = WALL
    print("Placed a wall at (7, 5).")

    player.move(1, 0, test_map) # Try to move right from (6, 5) into the wall at (7, 5)
    print(f"Tried to move right into wall. New Position: Coords({player.x}, {player.y})")
    assert player.x == 6 and player.y == 5 # Position should not change

    # --- Test 3: Transition to a new chunk ---
    player.x = CHUNK_WIDTH - 1 # Place player at the right edge
    print(f"Moved player to edge: ({player.x}, {player.y})")
    player.move(1, 0, test_map) # Move right to trigger transition
    print(f"Moved right across border. New Position: Chunk({player.chunk_x}, {player.chunk_y}), Coords({player.x}, {player.y})")
    assert player.chunk_x == 1 and player.x == 1

    print("\nPlayer movement tests passed!")