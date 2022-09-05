# The result of solution(n) represents the number of partitions of n with distinct parts.
# Partitions' order does not matter, but since we are building a staircase it might 
# help to view the partitions as being in descending order.
# The partition function for distinct partitions is represented by q(n).


def pentagonal(upto):
    k = 1
    n = 2
    while k <= upto:
        yield k
        if n % 2 == 0:
            m = n / 2
            k = m * (3 * m + 1) / 2
        else:
            m = (n + 1) / 2
            k = m * (3 * m - 1) / 2
        n += 1


def q(n, known_q):
    if n in known_q:
        return known_q[n]
    if n == 0:
        return 1
    m_disc = (1 + (12 * n))**0.5
    m_1 = (1 + m_disc)/6
    m_2 = (1 - m_disc)/6
    if m_1 % 1 == 0:
        a_k = (-1)**m_1
    elif m_2 % 1 == 0:
        a_k = (-1)**m_2
    else:
        a_k = 0
    q_n = int(a_k)
    sign = 1
    for p in pentagonal(n):
        if sign < 0:
            q_n -= q(n - p, known_q)
        else:
            q_n += q(n - p, known_q)
        if sign == -2:
            sign = 1
        else:
            sign -= 1
    known_q[n] = q_n
    return q_n

    

def solution(n):
    # The number of possible staircases is the number of distinct partitions - 1, 
    # since the staircase cannot simply be an 'n high' column 1 wide.
    return q(n, {}) - 1