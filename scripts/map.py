import random

# Import the visual assets from the central art repository.
from ascii_art import ROCK, BUSH, WALL, EMPTY

# Define constants for chunk dimensions
CHUNK_WIDTH = 80
CHUNK_HEIGHT = 24


class Map:
    """
    Manages the world map, including the procedural generation and storage of map chunks.
    """

    def __init__(self):
        """
        Initializes the map. A dictionary `self.chunks` will store the data
        for generated chunks, with (x, y) coordinates as keys.
        """
        self.chunks = {}
        # We don't generate the starting chunk here, we'll let the game do it
        # when it's ready.

    def get_chunk(self, chunk_x, chunk_y):
        """
        Retrieves a map chunk for the given chunk coordinates.

        If the chunk has not been generated yet, it calls the generation
        function, stores the result, and then returns it.
        """
        if (chunk_x, chunk_y) not in self.chunks:
            # This is a new, unexplored area, so we generate it.
            self.chunks[(chunk_x, chunk_y)] = self._generate_chunk(chunk_x, chunk_y)

        # Return the stored chunk data.
        return self.chunks[(chunk_x, chunk_y)]

    def _generate_chunk(self, chunk_x, chunk_y):
        """
        Generates a new map chunk filled with procedural content.
        For now, it's a bordered area with random rocks and bushes.
        """
        # Start with a chunk filled with empty tiles.
        chunk_data = [[EMPTY for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]

        # Create a solid border around the chunk. This helps in debugging and
        # will later serve as the boundary for player movement.
        for x in range(CHUNK_WIDTH):
            chunk_data[0][x] = WALL
            chunk_data[CHUNK_HEIGHT - 1][x] = WALL
        for y in range(CHUNK_HEIGHT):
            chunk_data[y][0] = WALL
            chunk_data[y][CHUNK_WIDTH - 1] = WALL

        # Sprinkle some random features (rocks and bushes) into the chunk.
        # We'll place a random number of features to make areas feel different.
        num_features = random.randint(15, 40)
        for _ in range(num_features):
            # Pick a random spot, avoiding the border walls.
            x = random.randint(1, CHUNK_WIDTH - 2)
            y = random.randint(1, CHUNK_HEIGHT - 2)

            # Choose a random feature type.
            feature = random.choice([ROCK, BUSH, BUSH]) # More bushes
            chunk_data[y][x] = feature

        return chunk_data


# This block allows for testing the map generation independently.
if __name__ == '__main__':
    print("--- Testing Map Generation ---")
    world_map = Map()

    # Generate the starting chunk.
    print("Generating chunk (0, 0)...")
    start_chunk = world_map.get_chunk(0, 0)

    # Print the generated chunk to the console for visual inspection.
    for row in start_chunk:
        print("".join(row))

    # Verify that the chunk is now stored in the map's cache.
    print(f"\nChunk (0, 0) is now cached: {(0, 0) in world_map.chunks}")

    # Retrieve the chunk again and check if it's the same object,
    # proving that it's being retrieved from cache instead of regenerated.
    retrieved_chunk = world_map.get_chunk(0, 0)
    print(f"Is retrieved chunk the same as the original? {retrieved_chunk is start_chunk}")