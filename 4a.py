import heapq

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


class PuzzleBoard:
    def __init__(self, state, parent=None, move="", cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()
        self.total_cost = self.cost + self.heuristic

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def calculate_heuristic(self):
        """
        Manhattan Distance heuristic
        """
        distance = 0

        for i in range(3):
            for j in range(3):
                value = self.state[i][j]

                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3

                    distance += abs(i - goal_x) + abs(j - goal_y)

        return distance

    def generate_successors(self):
        successors = []

        blank_x, blank_y = self.find_blank()

        moves = [
            (-1, 0, "up"),
            (1, 0, "down"),
            (0, -1, "left"),
            (0, 1, "right")
        ]

        for dx, dy, direction in moves:
            new_x = blank_x + dx
            new_y = blank_y + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]

                moved_tile = new_state[new_x][new_y]

                new_state[blank_x][blank_y], new_state[new_x][new_y] = (
                    new_state[new_x][new_y],
                    new_state[blank_x][blank_y]
                )

                move_description = f"Move {moved_tile} {opposite_direction(direction)}"

                successors.append(
                    PuzzleBoard(
                        new_state,
                        parent=self,
                        move=move_description,
                        cost=self.cost + 1
                    )
                )

        return successors

    def __lt__(self, other):
        return self.total_cost < other.total_cost


def opposite_direction(direction):
    if direction == "up":
        return "down"
    elif direction == "down":
        return "up"
    elif direction == "left":
        return "right"
    elif direction == "right":
        return "left"


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def reconstruct_path(node):
    path = []

    while node is not None:
        path.append(node)
        node = node.parent

    path.reverse()
    return path


def a_star_search(initial_state):
    start_node = PuzzleBoard(initial_state)

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
    print("Solution found!\n")

    for i, board in enumerate(solution):
        if i == 0:
            print("Initial State:")
        else:
            print(f"Move {i}: {board.move}")

        board.display()

    print("Sequence of Moves:")
    for i in range(1, len(solution)):
        print(f"Move {i}: {solution[i].move}")

else:
    print("No solution found.")