def generate_2d_automaton(rule, num_generations, grid_size):
    def apply_rule(rule_number, state, x, y):
        neighbors = [
            state[(x - 1) % grid_size][y],
            state[x][(y - 1) % grid_size],
            state[x][(y + 1) % grid_size],
            state[(x + 1) % grid_size][y],
        ]
        # Convert the neighborhood to a decimal value (binary to decimal)
        neighborhood = sum(neighbors[i] << i for i in range(4))
        # Apply the rule to determine the new state
        return (rule_number >> neighborhood) & 1

    initial_state = [[0] * grid_size for _ in range(grid_size)]
    initial_state[grid_size // 2][grid_size // 2] = 1

    automaton = [initial_state]

    for _ in range(num_generations - 1):
        current_state = automaton[-1]
        new_state = [[0] * grid_size for _ in range(grid_size)]

        for x in range(grid_size):
            for y in range(grid_size):
                new_state[x][y] = apply_rule(rule, current_state, x, y)

        automaton.append(new_state)

    return automaton
