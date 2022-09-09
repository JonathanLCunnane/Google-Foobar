def solution(M, F):
    M, F = int(M), int(F)
    gen = 0
    while True:
        if (M, F) == (1, 1):
            return str(gen)
        elif M <= 0 or F <= 0:
            return "impossible"
        if M == 1:
            return str(gen + F - M)
        if F == 1:
            return str(gen + M - F)
        if M > F:
            gen += M // F
            M %= F
        else:
            gen += F // M
            F %= M


print(solution(4, 7))