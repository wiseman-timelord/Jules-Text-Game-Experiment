import random
from perlin_noise import PerlinNoise

# Import the visual assets from the central art repository.
from ascii_art import ROCK, BUSH, WALL, EMPTY, WATER, PAVEMENT, BUILDINGS

# Define constants for chunk dimensions
CHUNK_WIDTH = 80
CHUNK_HEIGHT = 24

# --- Biome Definitions ---
# We use simple integer constants to represent each biome.
BIOME_OUTLANDS = 0
BIOME_URBAN = 1
# Add more biomes here in the future, e.g., BIOME_WASTELAND = 2


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
        # This noise layer is for determining biomes. It has a larger scale (lower frequency)
        # to create large, contiguous biome areas.
        self.biome_noise = PerlinNoise(octaves=2, seed=seed + 2)

        self.chunks = {}
        self.biome_map = {} # Cache for storing the biome of each chunk

    def get_chunk(self, chunk_x, chunk_y):
        """
        Retrieves a map chunk for the given chunk coordinates.

        If the chunk has not been generated yet, it calls the generation
        function, stores the result, and then returns it.
        """
        if (chunk_x, chunk_y) not in self.chunks:
            self.chunks[(chunk_x, chunk_y)] = self._generate_chunk(chunk_x, chunk_y)

        return self.chunks[(chunk_x, chunk_y)]

    def _get_biome(self, chunk_x, chunk_y):
        """
        Determines the biome for a given chunk using a large-scale Perlin noise map.
        The result is cached to ensure a chunk's biome remains constant.
        """
        if (chunk_x, chunk_y) in self.biome_map:
            return self.biome_map[(chunk_x, chunk_y)]

        # Use a much larger scale for biomes to make them span multiple chunks.
        biome_scale = 0.02
        noise_val = self.biome_noise([chunk_x * biome_scale, chunk_y * biome_scale])
        noise_val = (noise_val + 0.5)  # Normalize to 0-1 range

        # Decide biome based on the noise value.
        if noise_val < 0.5:
            biome = BIOME_OUTLANDS
        else:
            biome = BIOME_URBAN

        self.biome_map[(chunk_x, chunk_y)] = biome
        return biome

    def _generate_chunk(self, chunk_x, chunk_y):
        """
        Generates a new map chunk by first determining its biome and then
        calling the appropriate generation method for that biome.
        """
        biome = self._get_biome(chunk_x, chunk_y)

        if biome == BIOME_OUTLANDS:
            return self._generate_outlands_chunk(chunk_x, chunk_y)
        elif biome == BIOME_URBAN:
            return self._generate_urban_chunk(chunk_x, chunk_y)
        else:
            # Fallback to an empty chunk if biome is unknown
            return [[EMPTY for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]

    def _generate_outlands_chunk(self, chunk_x, chunk_y):
        """
        Generates a chunk for the "Outlands" biome, featuring natural terrain.
        This contains the original terrain generation logic.
        """
        chunk_data = [[EMPTY for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]
        scale = 0.05

        for y in range(CHUNK_HEIGHT):
            for x in range(CHUNK_WIDTH):
                global_x = (chunk_x * CHUNK_WIDTH) + x
                global_y = (chunk_y * CHUNK_HEIGHT) + y

                noise_val = self.noise([global_x * scale, global_y * scale])
                noise_val = (noise_val + 0.5)

                if noise_val < 0.35:
                    chunk_data[y][x] = WATER
                elif noise_val < 0.65:
                    feature_val = self.feature_noise([global_x * scale * 2, global_y * scale * 2])
                    feature_val = (feature_val + 0.5)
                    if feature_val > 0.8:
                        chunk_data[y][x] = BUSH
                    else:
                        chunk_data[y][x] = EMPTY
                elif noise_val < 0.8:
                    chunk_data[y][x] = ROCK
                else:
                    chunk_data[y][x] = ROCK

        # Draw a border around the chunk to contain the player.
        for x in range(CHUNK_WIDTH):
            chunk_data[0][x] = WALL
            chunk_data[CHUNK_HEIGHT - 1][x] = WALL
        for y in range(CHUNK_HEIGHT):
            chunk_data[y][0] = WALL
            chunk_data[y][CHUNK_WIDTH - 1] = WALL

        return chunk_data

    def _generate_urban_chunk(self, chunk_x, chunk_y):
        """
        Generates a chunk for the "Urban" biome, featuring pavement and complex buildings.
        """
        # Start with a base of pavement.
        chunk_data = [[PAVEMENT for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]
        building_noise = PerlinNoise(octaves=6, seed=self.feature_noise.seed)
        building_placer_scale = 0.2

        # A grid to mark where buildings are, to avoid overlap.
        occupied = [[False for _ in range(CHUNK_WIDTH)] for _ in range(CHUNK_HEIGHT)]

        # Iterate through potential building locations.
        for y in range(2, CHUNK_HEIGHT - 8): # Leave space for tall buildings
            for x in range(2, CHUNK_WIDTH - 12):
                if occupied[y][x]:
                    continue

                # Use noise to decide if we should place a building here.
                noise_val = building_noise([(chunk_x * CHUNK_WIDTH + x) * building_placer_scale,
                                            (chunk_y * CHUNK_HEIGHT + y) * building_placer_scale])
                noise_val = (noise_val + 0.5) # Normalize noise to 0-1 range

                if noise_val > 0.65:
                    # Choose a random building from the available assets
                    building_name = random.choice(list(BUILDINGS.keys()))
                    building_art = BUILDINGS[building_name]

                    b_height = len(building_art)
                    b_width = len(building_art[0])

                    # Check if the building fits and doesn't overlap with another.
                    if (x + b_width < CHUNK_WIDTH - 1 and
                        y + b_height < CHUNK_HEIGHT - 1 and
                        not any(occupied[iy][ix] for iy in range(y, y + b_height) for ix in range(x, x + b_width))):

                        # Place the building
                        for r, row_art in enumerate(building_art):
                            for c, char_art in enumerate(row_art):
                                if char_art != ' ': # Allow transparency
                                    chunk_data[y + r][x + c] = char_art
                                occupied[y + r][x + c] = True # Mark as occupied

                        # Mark a slightly larger area as occupied to create space between buildings
                        for iy in range(y, y + b_height + 2):
                           for ix in range(x, x + b_width + 2):
                               if iy < CHUNK_HEIGHT and ix < CHUNK_WIDTH:
                                   occupied[iy][ix] = True

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