import random

class ProceduralLevelGenerator:
    def __init__(self, level_width=55, level_height=35, amount_of_levels=100, remove_blocks=500):
        self.level_width = level_width
        self.level_height = level_height
        self.amount_of_levels = amount_of_levels
        self.remove_blocks = remove_blocks

    def get_level_row(self):
        return ['#'] * self.level_width

    def get_wall_level(self):
        return [self.get_level_row() for _ in range(self.level_height)]

    def drunken_walk_generator(self):
        drunk = {
            'removeBlocks': self.remove_blocks,
            'padding': 2,
            'x': int(self.level_width / 2),
            'y': int(self.level_height / 2)
        }

        start_coordinate = [drunk['x'], drunk['y']]

        level = self.get_wall_level()

        x = -1
        y = -1

        while drunk['removeBlocks'] >= 0:
            x = drunk['x']
            y = drunk['y']

            if level[y][x] == '#':
                level[y][x] = '.'
                drunk['removeBlocks'] -= 1

            roll = random.randint(1, 4)

            if roll == 1 and x > drunk['padding']:
                drunk['x'] -= 1
            if roll == 2 and x < self.level_width - 1 - drunk['padding']:
                drunk['x'] += 1
            if roll == 3 and y > drunk['padding']:
                drunk['y'] -= 1
            if roll == 4 and y < self.level_height - 1 - drunk['padding']:
                drunk['y'] += 1

        end_coordinate = [x, y]

        return [level, start_coordinate, end_coordinate]

    def get_next_moves(self, x, y):
        return {
            'left': [x-1, y],
            'right': [x+1, y],
            'up': [x, y-1],
            'down': [x, y+1]
        }.values()

    def get_shortest_path(self, level, start_coordinate, end_coordinate):
        search_paths = [[start_coordinate]]
        visited_coordinates = [start_coordinate]

        while search_paths != []:
            current_path = search_paths.pop(0)
            current_coordinate = current_path[-1]

            current_x, current_y = current_coordinate

            if current_coordinate == end_coordinate:
                return current_path

            for next_coordinate in self.get_next_moves(current_x, current_y):
                next_x, next_y = next_coordinate

                if next_x < 0 or next_x >= self.level_width:
                    continue

                if next_y < 0 or next_y >= self.level_height:
                    continue

                if next_coordinate in visited_coordinates:
                    continue

                if level[next_y][next_x] == '#':
                    continue

                search_paths.append(current_path + [next_coordinate])
                visited_coordinates += [next_coordinate]

        return []

    def generate_levels(self):
        return [self.drunken_walk_generator() for _ in range(self.amount_of_levels)]

    def evaluate_levels(self, levels):
        evaluation_scores = []

        for generated_level, start_coordinate, end_coordinate in levels:
            shortest_solution = self.get_shortest_path(
                generated_level,
                start_coordinate,
                end_coordinate
            )

            evaluation_scores.append(
                [len(shortest_solution), generated_level]
            )

        return evaluation_scores

    def generate_best_level(self):
        levels = self.generate_levels()

        evaluation_scores = self.evaluate_levels(levels)

        evaluation_scores.sort()
        evaluation_scores.reverse()

        score, best_level = evaluation_scores.pop(0)

        return best_level

    def print_best_level(self):
        best_level = self.generate_best_level()
        for row in best_level:
            print(''.join(row))





