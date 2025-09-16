class EightPuzzle:
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """
        Eight Puzzle Problem definition.

        initial: tuple of length 9 representing the start state
        goal:    tuple of length 9 representing the goal state (default: canonical solved puzzle)
        """
        self.initial = tuple(initial)
        self.goal = tuple(goal)

    def actions(self, state):
        """Return list of possible moves for the blank (0)."""
        index = state.index(0)
        row, col = divmod(index, 3)
        moves = []
        if row > 0: moves.append("UP")
        if row < 2: moves.append("DOWN")
        if col > 0: moves.append("LEFT")
        if col < 2: moves.append("RIGHT")
        return moves

    def result(self, state, action):
        """Return new state and descriptive move string."""
        index = state.index(0)
        row, col = divmod(index, 3)
        new_state = list(state)

        if action == "UP":
            swap_index = (row - 1) * 3 + col
            tile = state[swap_index]
            move_name = f"Move {tile} Down"
        elif action == "DOWN":
            swap_index = (row + 1) * 3 + col
            tile = state[swap_index]
            move_name = f"Move {tile} Up"
        elif action == "LEFT":
            swap_index = row * 3 + (col - 1)
            tile = state[swap_index]
            move_name = f"Move {tile} Right"
        elif action == "RIGHT":
            swap_index = row * 3 + (col + 1)
            tile = state[swap_index]
            move_name = f"Move {tile} Left"
        else:
            raise ValueError(f"Invalid action: {action}")

        # swap blank with the target tile
        new_state[index], new_state[swap_index] = new_state[swap_index], new_state[index]
        return tuple(new_state), move_name

    def action_cost(self, s, a, s_prime):
        """Each move costs 1 by default."""
        return 1

    def is_goal(self, state):
        """Check if the state is the goal."""
        return state == self.goal

    def is_solvable(self, state=None):
        """Check solvability using inversion count (for odd-width board)."""
        if state is None:
            state = self.initial

        one_d = [tile for tile in state if tile != 0]
        inversions = sum(1 for i in range(len(one_d)) for j in range(i+1, len(one_d)) if one_d[i] > one_d[j])
        return inversions % 2 == 0


def expand(problem, node):
    """Generate child nodes with descriptive moves."""
    for action in problem.actions(node.state):
        s_prime, move_name = problem.result(node.state, action)
        cost = node.path_cost + problem.action_cost(node.state, action, s_prime)
        yield Node(state=s_prime, parent=node, action=move_name,
                   path_cost=cost, depth=node.depth + 1)
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0, f_val=0):
        self.state = state          # 8-puzzle board (tuple of 9 numbers)
        self.parent = parent        # pointer to parent Node
        self.action = action        # move taken to reach this state (e.g. "Move 7 Left")
        self.path_cost = path_cost  # g(n): cost from start
        self.depth = depth          # depth in the search tree
        self.f_val = f_val          # priority value (for UCS, Greedy, A*)

    def __lt__(self, other):
        """
        Compare nodes by their f_val (priority).
        If equal, compare by path_cost (g(n)) to break ties.
        """
        if self.f_val == other.f_val:
            return self.path_cost < other.path_cost
        return self.f_val < other.f_val


# Heuristics
def misplaced_tiles(node, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    return sum(1 for i, tile in enumerate(node.state) if tile != 0 and tile != goal[i])


def manhattan_distance(node, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    distance = 0
    for i, tile in enumerate(node.state):
        if tile != 0:
            goal_index = goal.index(tile)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
