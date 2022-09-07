def xor(n): # xor's consecutive values from 1 to n
    rem = n % 4
    if rem == 0:
        return n
    elif rem == 1:
        return 1
    elif rem == 2:
        return n + 1
    return 0


def solution(start, length):
    checksum = 0
    for line in range(length):
        # For each line xor between l and r.
        # Since a ^ a= 0, and a ^ 0 = 0
        # xor of all vals between l and r is just xor(l-1) ^ xor(r)
        l = start + length*line
        r = l + length - line - 1
        checksum ^= xor(l - 1) ^ xor(r)
    return checksum