import datetime

class Logger:
    def __init__(self, enabled=False, args=None):
        self.enabled = enabled
        if enabled:
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            self.file = open(f"trace-{ts}.txt", "w", encoding="utf-8")
            if args:
                self.file.write(f"Command-Line Arguments: {args}\n")
        else:
            self.file = None

    def write(self, message):
        if self.enabled:
            self.file.write(message + "\n")

    def close(self):
        if self.enabled:
            self.file.close()


def format_state(state):
    """Return 3x3 list representation for pretty printing."""
    return [[state[i*3 + j] for j in range(3)] for i in range(3)]


def format_node(node):
    """Format node as required in trace."""
    action = node.action if node.action else "Start"
    return (f"< state = {format_state(node.state)}, "
            f"action = {{{action}}} "
            f"g(n) = {node.path_cost}, d = {node.depth}, "
            f"f(n) = {node.f_val}, "
            f"Parent = Pointer to {{{'None' if not node.parent else format_node_brief(node.parent)}}} >")


def format_node_brief(node):
    action = node.action if node.action else "Start"
    return (f"< state = {format_state(node.state)}, "
            f"action = {{{action}}} "
            f"g(n) = {node.path_cost}, d = {node.depth}, ... >")

def reconstruct_path(node):
    """Return sequence of (action, state) from root to goal."""
    path = []
    while node:
        path.append((node.action, node.state, node.depth, node.path_cost))
        node = node.parent
    return list(reversed(path))[1:]  # skip root (None action)

def print_solution(solution, stats):
    """Pretty print final stats and solution steps to console."""
    if solution is None:
        print("No solution found.")
        return

    path = reconstruct_path(solution)
    depth = path[-1][2]
    cost = path[-1][3]

    print(f"Nodes Popped: {stats['popped']}")
    print(f"Nodes Expanded: {stats['expanded']}")
    print(f"Nodes Generated: {stats['generated']}")
    print(f"Max Fringe Size: {stats['max_fringe']}")
    print(f"Solution Found at depth {depth} with cost of {cost}.")
    print("Steps:")
    for action, _, _, _ in path:
        print(f"\t{action}")


def log_solution(logger, solution, stats):
    """Write final solution and stats into the trace file."""
    if solution is None:
        logger.write("No solution found.")
        return

    path = reconstruct_path(solution)
    depth = path[-1][2]
    cost = path[-1][3]

    logger.write("\n=== Final Solution ===")
    logger.write(f"Nodes Popped: {stats['popped']}")
    logger.write(f"Nodes Expanded: {stats['expanded']}")
    logger.write(f"Nodes Generated: {stats['generated']}")
    logger.write(f"Max Fringe Size: {stats['max_fringe']}")
    logger.write(f"Solution Found at depth {depth} with cost of {cost}.")
    logger.write("Steps:")
    for action, state, _, _ in path:
        logger.write(f"\t{action}")