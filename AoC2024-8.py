from itertools import combinations

def parse_map(input_data):
    """Parse the input map into a list of antenna coordinates and frequencies."""
    antennas = []
    for y, line in enumerate(input_data.strip().split("\n")):
        for x, char in enumerate(line):
            if char.isalnum():
                antennas.append((x, y, char))
    return antennas

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def find_antinodes(antennas, width, height):
    """Find all unique antinodes within the bounds of the map."""
    antinodes = set()

    # Group antennas by frequency
    frequency_groups = {}
    for x, y, freq in antennas:
        if freq not in frequency_groups:
            frequency_groups[freq] = []
        frequency_groups[freq].append((x, y))

    # Process each frequency group
    for freq, group in frequency_groups.items():
        # Add all antenna positions as antinodes
        for x, y in group:
            antinodes.add((x, y))

        # Check all pairs of antennas with the same frequency
        for (x1, y1), (x2, y2) in combinations(group, 2):
            # Calculate the step (dx, dy) for the line
            dx, dy = x2 - x1, y2 - y1
            step = gcd(dx, dy)
            dx //= step
            dy //= step

            # Extend line in both directions and add points
            px, py = x1, y1
            while 0 <= px < width and 0 <= py < height:
                antinodes.add((px, py))
                px -= dx
                py -= dy

            px, py = x1 + dx, y1 + dy
            while 0 <= px < width and 0 <= py < height:
                antinodes.add((px, py))
                px += dx
                py += dy

    return antinodes

# Read input from file
file_path = r"C:\Users\MatthewSilbernagel\Desktop\input.txt"
with open(file_path, 'r') as file:
    data = file.read()

# Parse map and find antinodes
antennas = parse_map(data)
height = len(data.strip().split("\n"))
width = max(len(line) for line in data.strip().split("\n"))

antinodes = find_antinodes(antennas, width, height)
print("Total Unique Antinode Locations:", len(antinodes))
