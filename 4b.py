import heapq

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


class PuzzleNode:
    def __init__(self, state, parent=None, move="", g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = self.manhattan_distance()
        self.f = self.g + self.h

    def manhattan_distance(self):
        distance = 0

        for i in range(3):
            for j in range(3):
                tile = self.state[i][j]

                if tile != 0:
                    goal_row = (tile - 1) // 3
                    goal_col = (tile - 1) % 3

                    distance += abs(i - goal_row) + abs(j - goal_col)

        return distance

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        blank_row, blank_col = self.find_blank()

        moves = [
            (-1, 0, "down"),
            (1, 0, "up"),
            (0, -1, "right"),
            (0, 1, "left")
        ]

        for row_change, col_change, direction in moves:
            new_row = blank_row + row_change
            new_col = blank_col + col_change

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]

                moved_tile = new_state[new_row][new_col]

                new_state[blank_row][blank_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[blank_row][blank_col]
                )

                move_description = f"Move {moved_tile} {direction}"

                successors.append(
                    PuzzleNode(
                        new_state,
                        parent=self,
                        move=move_description,
                        g=self.g + 1
                    )
                )

        return successors

    def display(self):
        for row in self.state:
            print(row)
        print()

    def __lt__(self, other):
        return self.f < other.f


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def reconstruct_path(node):
    path = []

    while node is not None:
        path.append(node)
        node = node.parent

    return path[::-1]


def a_star_search(initial_state):
    start_node = PuzzleNode(initial_state)

    open_list = []
    heapq.heappush(open_list, start_node)

    visited = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.is_goal():
            return reconstruct_path(current_node)

        visited.add(state_to_tuple(current_node.state))

        for successor in current_node.generate_successors():
            if state_to_tuple(successor.state) not in visited:
                heapq.heappush(open_list, successor)

    return None


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = a_star_search(initial_state)

if solution:
    print("Solution found using A* Search Algorithm\n")

    for i, node in enumerate(solution):
        if i == 0:
            print("Initial State:")
        else:
            print(f"Move {i}: {node.move}")

        node.display()

    print("Sequence of Moves:")
    for i in range(1, len(solution)):
        print(f"Move {i}: {solution[i].move}")

else:
    print("No solution found.")