
initial_8_puzzle = [[2, 3, 6],
                    [1, 0, 7],
                    [4, 8 ,5]]

final_8_puzzle = [[1 ,2 ,3],
                  [4 ,5 ,6],
                  [7 ,8 ,0] ]


def position0(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return (i ,j)
    return None


initialPosition = position0(initial_8_puzzle)



def validMoves(pos):

    moves = {(0 ,0) :('b' ,'r'), (0 ,1) :('l' ,'r' ,'b'), (0 ,2) :('l' ,'b'),
             (1 ,0) :('u' ,'b' ,'r'), (1 ,1) :('u' ,'r' ,'b' ,'l'), (1 ,2) :('u' ,'l' ,'b'),
             (2 ,0) :('u' ,'r'), (2 ,1) :('l' ,'r' ,'u'), (2 ,2) :('l' ,'u') ,}

    if pos in moves:
        return moves[pos]
    else:
        return None

possibleMoves = validMoves(initialPosition)
print(possibleMoves)


def actions(puzzle, act, pos_0):
    x, y = pos_0
    # fresh independent copy using list comprehension
    new_puzzle = [row[:] for row in puzzle]

    if act == 'u' and x > 0:
        new_puzzle[x][y], new_puzzle[ x -1][y] = new_puzzle[ x -1][y], new_puzzle[x][y]

    elif act == 'l' and y > 0:
        new_puzzle[x][y], new_puzzle[x][ y -1] = new_puzzle[x][ y -1], new_puzzle[x][y]

    elif act == 'r' and y < len(puzzle[0]) - 1:
        new_puzzle[x][y], new_puzzle[x][ y +1] = new_puzzle[x][ y +1], new_puzzle[x][y]

    elif act == 'b' and x < len(puzzle) - 1:
        new_puzzle[x][y], new_puzzle[ x +1][y] = new_puzzle[ x +1][y], new_puzzle[x][y]

    return new_puzzle




class Node:
    def __init__(self, puzzle, parent='initial' ,action='initial', path_cost=0, state=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.pos_0 = position0(puzzle)
        self.state_no = state
        self.possibleMoves = ()

    def displayNode(self):
        print(self.pos_0)
        print(self.puzzle)
        print(self.state_no)

    def position0(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def validateGoal(self ,finalPuzzle):
        if self.puzzle == finalPuzzle:
            print("Goal State")
            return True

        else:
            print("Yet to continue.")
            return False

    def validMoves(self, pos_0):

        moves = {(0, 0): ('b', 'r'), (0, 1): ('l', 'r', 'b'), (0, 2): ('l', 'b'),
                 (1, 0): ('u', 'b', 'r'), (1, 1): ('u', 'r', 'b', 'l'), (1, 2): ('u', 'l', 'b'),
                 (2, 0): ('u', 'r'), (2, 1): ('l', 'r', 'u'), (2, 2): ('l', 'u'), }

        if pos_0 in moves:
            self.possibleMoves = moves[pos_0]
        else:
            return None
        print(self.possibleMoves)

# actions(initial_8_puzzle, 'b', initialPosition)

# Node1 = Node(initial_8_puzzle, initialPosition, "S1")
#
# Node1.displayNode()
# Node1.validMoves(initialPosition)
# Node1.validateGoal(initial_8_puzzle)

# class BFS:
#     def __init__(self,node):
#
#
#     def implement(self):


class AI:
    def __init__(self, node ):
        self.node = node
        self.result = None
        self.frontier = []
        self.initial_node = []
        self.reached = []
        self.s = ""
        self.expanded = {}

    def expandNode(self):
        print('From node1')
        moves = self.node.validMoves(self.node.pos_0)
        print(moves)
        self.s = self.node.state_no
        print(self.node.possibleMoves)
        for i, action in enumerate(self.node.possibleMoves):
            # print(i+1,action)
            self.result = actions(self.node.puzzle, action, self.node.pos_0)
            # print(actions(self.node.puzzle, action, self.node.pos_0))
            # print(actions(node.puzzle, action, node.pos_0))
            self.expanded[ i +1] = Node(self.result, self.node.parent, action, i+ 1)

        print(self.expanded)
        #
        # print(f'Nodes Expanded: {self.expanded}')

    def bfs(self, node):

        if node.validateGoal():
            return node

        self.frontier.append(node.state_no)
        self.reached.append(node.state_no)

        while self.frontier != []:
            node = self.frontier.pop()


node1 = Node(initial_8_puzzle)
node1.displayNode()

expanded = AI(node1)
expanded.expandNode()











