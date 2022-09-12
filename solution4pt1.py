from itertools import combinations



def solution(num_buns, num_required):
    # If the required amount of bunnies is x, and the number of bunnies y,
    # For a set of x - 1 bunnies, there has to be at least one key that is
    # not represented at all. This means that for each set of y - (x - 1)
    # or y - x + 1 bunnies, there is a key which is only held by that set.
    # For any set of x bunnies, there needs to be every key represented
    # at least once. Therefore each key needs to be represented
    # by at least y - x + 1 bunnies
    # 
    # Hence each set of y - x + 1 bunnies can be given a key. 
    # We will call these sets the key sets.
    buns = [[] for bun in range(num_buns)]
    key_sets = combinations(range(num_buns), num_buns - num_required + 1)
    for key, curr_buns in enumerate(key_sets):
        for curr_bun in curr_buns:
            buns[curr_bun].append(key)
    return buns