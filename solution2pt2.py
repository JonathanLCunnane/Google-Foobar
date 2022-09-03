from itertools import product



# Get invalid moves for each square
invalid_moves = {}
invalid_moves[0] = [-17, -15, -10, -6, 6, 15]
invalid_moves[1] = [-17, -15, -10, -6, 6]
for i in range(2, 6): invalid_moves[i] = [-17, -15, -10, -6]
invalid_moves[6] = [-17, -15, -10, -6, 10]
invalid_moves[7] = [-17, -15, -10, -6, 10, 17]
invalid_moves[8] = [-17, -15, -10, 6, 15]
invalid_moves[9] = [-17, -15, -10, 6]
for i in range(10, 14): invalid_moves[i] = [-17, -15]
invalid_moves[14] = [-17, -15, -6, 10]
invalid_moves[15] = [-17, -15, -6, 10, 17]
for i in range(16, 48, 8): invalid_moves[i] = [-17, -10, 6, 15]
for i in range(17, 49, 8): invalid_moves[i] = [-10, 6]
for i in range(1, 5):
    for j in range(17 + i, 49 + i, 8): invalid_moves[j] = []
for i in range(22, 54, 8): invalid_moves[i] = [-6, 10]
for i in range(23, 55, 8): invalid_moves[i] = [-15, -6, 10, 17]
invalid_moves[48] = [-17, -10, 6, 15, 17]
invalid_moves[49] = [-10, 6, 15, 17]
for i in range(50, 54): invalid_moves[i] = [15, 17]
invalid_moves[54] = [-6, 10, 15, 17]
invalid_moves[55] = [-15, -6, 10, 15, 17]
invalid_moves[56] = [-17, -10, 6, 10, 15, 17]
invalid_moves[57] = [-10, 6, 10, 15, 17]
for i in range(58, 62): invalid_moves[i] = [6, 10, 15, 17]
invalid_moves[62] = [-6, 6, 10, 15, 17]
invalid_moves[63] = [-15, -6, 6, 10, 15, 17]


def solution(src, dest):
    if src == dest:
        return 0
    n = 1
    vals = [-17, -15, -10, -6, 6, 10, 15, 17]
    while True:
        perms = product(vals, repeat=n)
        # Validate each permutation while traversing.
        # Break if permutation becomes invalid.
        for perm in perms:
            pos = src
            for move in perm:
                if move in invalid_moves[pos]:
                    break
                pos += move
                if pos == dest:
                    return n
        n += 1


for i in range(0, 64):
    for j in range(0, 64):
        solution(i, j)