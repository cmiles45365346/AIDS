import random


#review time: 1668128107.0732753
def get_random_number_in_range(low_value, high_value):
    return random.randint(low_value, high_value)  # Generates pseudo random number between 1 and 5000 for generation


# Generates terrain in square area around player
#review time: 1668128107.0732753
def generate_cells(screen_x, screen_y, screen_dimensions):
    terrain = []  # Start with blank terrain
    for x in range(screen_dimensions):
        for y in range(screen_dimensions):
            # Get seed for pseudo-randomness
            random.seed(x + screen_x + ((y + screen_y) * screen_dimensions))
            random_number = get_random_number_in_range(0, 5000)  # generate cell number based off seed used

            if x + screen_x > 500 or x + screen_x < -500 or y + screen_y < -500 or y + screen_y > 500:  # World borders
                terrain.append("∧") # Generates mountains as world border
            elif random_number < 1235:  # Generates upwards grass tile
                terrain.append("8")
            elif random_number < 2470:  # Generates right grass tiles
                terrain.append("6")
            elif random_number < 3705:  # Generates down grass tile
                terrain.append("2")
            elif random_number < 4940:  # Generates left grass tile
                terrain.append("4")
            elif random_number < 4982:  # Generates mountains
                terrain.append("∧")
            elif random_number < 5001:  # Generates traders
                terrain.append("a")
            else:
                terrain.append("~")
    return terrain  # Returns generated terrain as output
