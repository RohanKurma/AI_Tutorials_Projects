from collections import deque
import heapq
from eightPuzzleProblem import Node, expand
from utils import Logger, format_node, format_state, log_solution


def init_stats():
    return {"popped": 0, "expanded": 0, "generated": 0, "max_fringe": 0}

# ---------------------------
# Breadth-First Search
# ---------------------------
def breadth_first_search(problem, trace=False):
    logger = Logger(trace)
    stats = init_stats()
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        logger.close()
        return node, stats

    frontier = deque([node])
    reached = {problem.initial}

    logger.write("After Initialization")
    logger.write(f"\tClosed: []")
    logger.write(f"\tFringe: [{format_node(node)}]")
    logger.write(f"\tNodes Popped: 0")
    logger.write(f"\tNodes Expanded: 0")
    logger.write(f"\tNodes Generated: 1")
    logger.write(f"\tMax Fringe Size: 1")

    while frontier:
        stats["max_fringe"] = max(stats["max_fringe"], len(frontier))
        node = frontier.popleft()
        stats["popped"] += 1
        stats["expanded"] += 1

        logger.write(f"Generating successors to {format_node(node)}:")
        successors = list(expand(problem, node))
        logger.write(f"\t{len(successors)} successors generated")
        logger.write(f"\tClosed: { [format_state(node.state)] }")

        for child in successors:
            stats["generated"] += 1
            if problem.is_goal(child.state):
                logger.close()
                return child, stats
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)

        logger.write("\tFringe: [")
        for c in frontier:
            logger.write("\t\t" + format_node(c))
        logger.write("\t]")
        logger.write(f"\tNodes Popped: {stats['popped']}")
        logger.write(f"\tNodes Expanded: {stats['expanded']}")
        logger.write(f"\tNodes Generated: {stats['generated']}")
        logger.write(f"\tMax Fringe Size: {stats['max_fringe']}")

    log_solution(logger, None, stats)
    logger.close()
    return None, stats

# ---------------------------
# General Best-First Framework (for UCS, Greedy, A*)
# ---------------------------
def best_first_search(problem, f, trace=False, args=None):
    logger = Logger(trace, args)
    stats = init_stats()
    node = Node(problem.initial)
    node.f_val = f(node)
    frontier = []
    heapq.heappush(frontier, node)
    reached = {problem.initial: node}

    logger.write("After Initialization")
    logger.write(f"\tClosed: []")
    logger.write(f"\tFringe: [{format_node(node)}]")
    logger.write(f"\tNodes Popped: 0")
    logger.write(f"\tNodes Expanded: 0")
    logger.write(f"\tNodes Generated: 1")
    logger.write(f"\tMax Fringe Size: 1")

    closed = []

    while frontier:
        stats["max_fringe"] = max(stats["max_fringe"], len(frontier))
        node = heapq.heappop(frontier)
        stats["popped"] += 1

        if problem.is_goal(node.state):
            logger.close()
            return node, stats

        stats["expanded"] += 1
        logger.write(f"Generating successors to {format_node(node)}:")
        successors = list(expand(problem, node))
        logger.write(f"\t{len(successors)} successors generated")

        closed.append(format_state(node.state))
        logger.write(f"\tClosed: {closed}")

        for child in successors:
            stats["generated"] += 1
            child.f_val = f(child)
            if (child.state not in reached) or (child.path_cost < reached[child.state].path_cost):
                reached[child.state] = child
                heapq.heappush(frontier, child)

        logger.write("\tFringe: [")
        for c in sorted(frontier, key=lambda x: x.f_val):
            logger.write("\t\t" + format_node(c))
        logger.write("\t]")
        logger.write(f"\tNodes Popped: {stats['popped']}")
        logger.write(f"\tNodes Expanded: {stats['expanded']}")
        logger.write(f"\tNodes Generated: {stats['generated']}")
        logger.write(f"\tMax Fringe Size: {stats['max_fringe']}")
    log_solution(logger, None, stats)
    logger.close()
    return None, stats

# ---------------------------
# Algorithm Wrappers
# ---------------------------
def uniform_cost_search(problem, trace=False, args=None):
    return best_first_search(problem, f=lambda n: n.path_cost, trace=trace, args=args)

def greedy_best_first(problem, h, trace=False, args=None):
    return best_first_search(problem, f=lambda n: h(n), trace=trace, args=args)

def a_star_search(problem, h, trace=False, args=None):
    return best_first_search(problem, f=lambda n: n.path_cost + h(n), trace=trace, args=args)

# ---------------------------
# Depth-First Search
# ---------------------------
def depth_first_search(problem, trace=False, limit=None, args= None):
    logger = Logger(trace, args)
    stats = init_stats()
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        logger.close()
        return node, stats

    frontier = [node]
    reached = {problem.initial}
    closed = []

    while frontier:
        stats["max_fringe"] = max(stats["max_fringe"], len(frontier))
        node = frontier.pop()
        stats["popped"] += 1
        stats["expanded"] += 1

        logger.write(f"Expanding {format_node(node)}")
        successors = list(expand(problem, node))
        logger.write(f"\t{len(successors)} successors generated")
        closed.append(format_state(node.state))
        logger.write(f"\tClosed: {closed}")

        if limit is not None and node.depth >= limit:
            continue  # cutoff

        for child in successors:
            stats["generated"] += 1
            if problem.is_goal(child.state):
                logger.close()
                return child, stats
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)

        logger.write("\tFringe: [")
        for c in frontier:
            logger.write("\t\t" + format_node(c))
        logger.write("\t]")
    log_solution(logger, None, stats)
    logger.close()
    return None, stats

def depth_limited_search(problem, limit, trace=False, args= None):
    return depth_first_search(problem, trace=trace, limit=limit, args=args)

def iterative_deepening_search(problem, trace=False, args= None):
    depth = 0
    stats = init_stats()
    while True:
        node, s = depth_limited_search(problem, depth, trace=trace, args=args)
        for k in stats: stats[k] += s[k]
        if node: return node, stats
        depth += 1
