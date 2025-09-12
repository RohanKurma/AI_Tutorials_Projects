

initial_8_puzzle = [[2, 3, 6],
                    [1, 0, 7],
                    [4, 8,5]]

final_8_puzzle = [[1,2,3],
                  [4,5,6],
                  [7,8,0] ]


def position0(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return (i,j)
    return None


initialPosition = position0(initial_8_puzzle)



def validMoves(pos):

    moves = {(0,0):('b','r'), (0,1):('l','r','b'), (0,2):('l','b'),
             (1,0):('u','b','r'), (1,1):('u','r','b','l'), (1,2):('u','l','b'),
             (2,0):('u','r'), (2,1):('l','r','u'), (2,2):('l','u'),}

    if pos in moves:
        return moves[pos]
    else:
        return None

possibleMoves = validMoves(initialPosition)
print(possibleMoves)


def actions(puzzle, act, pos_0):

    x, y = pos_0

    if act == 'u':

        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]

    if act == 'l':
        p
actions(initial_8_puzzle, 'u', initialPosition)
