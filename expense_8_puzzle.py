import argparse
import sys
from eightPuzzleProblem import EightPuzzle, manhattan_distance
from searchAlgorithms import breadth_first_search, uniform_cost_search, \
                              depth_first_search, depth_limited_search, \
                              iterative_deepening_search, greedy_best_first, a_star_search
from utils import print_solution
def read_puzzle(filename):
    with open(filename, "r") as f:
        numbers = [int(x) for line in f for x in line.split()]
    return tuple(numbers)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_file")
    parser.add_argument("goal_file")
    parser.add_argument("method", nargs="?", default="a*")
    parser.add_argument("-d", "--dump", action="store_true")
    args = parser.parse_args()

    trace = args.dump
    cli_args = sys.argv + ([str(trace).lower()] if trace else [])

    start = read_puzzle(args.start_file)
    goal = read_puzzle(args.goal_file)

    problem = EightPuzzle(start, goal)

    method = args.method.lower()
    if method == "bfs":
        solution, stats = breadth_first_search(problem, trace=args.dump, args=cli_args)
    elif method == "ucs":
        solution, stats = uniform_cost_search(problem, trace=args.dump, args=cli_args)
    elif method == "dfs":
        solution, stats = depth_first_search(problem, trace=args.dump, args=cli_args)
    elif method == "dls":
        limit = int(input("Enter depth limit: "))
        solution, stats = depth_limited_search(problem, limit, trace=args.dump, args=cli_args)
    elif method == "ids":
        solution, stats = iterative_deepening_search(problem, trace=args.dump, args=cli_args)
    elif method == "greedy":
        solution, stats = greedy_best_first(problem, manhattan_distance, trace=args.dump, args=cli_args)
    elif method == "a*":
        solution, stats = a_star_search(problem, manhattan_distance, trace=args.dump, args=cli_args)
    else:
        print(f"Unknown method: {method}")
        return

    if solution:
        print_solution(solution, stats)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
