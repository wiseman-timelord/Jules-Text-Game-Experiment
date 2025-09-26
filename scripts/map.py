import random
from perlin_noise import PerlinNoise

# Import the visual assets from the central art repository.
from ascii_art import ROCK, BUSH, WALL, EMPTY, WATER

# Define constants for chunk dimensions
CHUNK_WIDTH = 80
CHUNK_HEIGHT = 24


class Map:
    """
    Manages the world map, including the procedural generation and storage of map chunks.
    """

    def __init__(self, seed=None):
        """
        Initializes the map. A dictionary `self.chunks` will store the data
        for generated chunks, with (x, y) coordinates as keys.

        Args:
            seed (int, optional): A seed for the Perlin Noise generator to ensure
                                  reproducible maps. Defaults to None (random).
        """
        if seed is None:
            seed = random.randint(0, 100000)

        # Initialize Perlin noise generators for different features.
        # Using different seeds and octaves creates more varied terrain.
        self.noise = PerlinNoise(octaves=4, seed=seed)
        self.feature_noise = PerlinNoise(octaves=8, seed=seed + 1)
        self.chunks = {}

    def get_chunk(self, chunk_x, chunk_y):
        """
        Retrieves a map chunk for the given chunk coordinates.

        If the chunk has not been generated yet, it calls the generation
        function, stores the result, and then returns it.
        """
        if (chunk_x, chunk_y) not in self.chunks:
            self.chunks[(chunk_x, chunk_y)] = self._generate_chunk(chunk_x, chunk_y)

        return self.chunks[(chunk_x, chunk_y)]

    def _generate_chunk(self, chunk_x, chunk_y):
        """
        Generates a new map chunk using Perlin noise for natural terrain.
        """
        chunk_data = [[EMPTY for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]

        # Scale determines the "zoom" level of the noise. Smaller values = larger features.
        scale = 0.05

        for y in range(CHUNK_HEIGHT):
            for x in range(CHUNK_WIDTH):
                # Calculate global coordinates to ensure seamless chunk transitions.
                global_x = (chunk_x * CHUNK_WIDTH) + x
                global_y = (chunk_y * CHUNK_HEIGHT) + y

                # Generate noise value. The library returns values from -0.5 to 0.5.
                # We normalize it to a 0.0 to 1.0 range for easier use with thresholds.
                noise_val = self.noise([global_x * scale, global_y * scale])
                noise_val = (noise_val + 0.5) # Shift to 0-1 range

                # Apply thresholds to determine the base terrain type.
                if noise_val < 0.35:
                    chunk_data[y][x] = WATER
                elif noise_val < 0.65:
                    # This is our "grassland" area, add features on top.
                    feature_val = self.feature_noise([global_x * scale * 2, global_y * scale * 2])
                    feature_val = (feature_val + 0.5)
                    if feature_val > 0.8:
                        chunk_data[y][x] = BUSH
                    else:
                        chunk_data[y][x] = EMPTY
                elif noise_val < 0.8:
                    chunk_data[y][x] = ROCK
                else:
                    # Higher elevations are rockier
                    chunk_data[y][x] = ROCK

        # Draw a border around the chunk to contain the player.
        for x in range(CHUNK_WIDTH):
            chunk_data[0][x] = WALL
            chunk_data[CHUNK_HEIGHT - 1][x] = WALL
        for y in range(CHUNK_HEIGHT):
            chunk_data[y][0] = WALL
            chunk_data[y][CHUNK_WIDTH - 1] = WALL

        return chunk_data


# This block allows for testing the new map generation independently.
if __name__ == '__main__':
    print("--- Testing Perlin Noise Map Generation ---")
    # Use a fixed seed for reproducible test output
    world_map = Map(seed=123)

    # Generate the starting chunk.
    print("Generating chunk (0, 0)...")
    start_chunk = world_map.get_chunk(0, 0)

    # Print the generated chunk to the console for visual inspection.
    for row in start_chunk:
        print("".join(row))

    print(f"\nChunk (0, 0) is now cached: {(0, 0) in world_map.chunks}")