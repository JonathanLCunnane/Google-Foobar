"""There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme. 

Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000."""


def is_prime(n):
    if n % 3 == 0:
        return False
    for curr in range(5, int(n ** 0.5) + 1, 6):
        if n % curr == 0:
            return False
        if n % (curr + 2) == 0:
            return False
    return True


def primes():
    yield 2
    yield 3
    n = 5
    while True:
        if is_prime(n):
            yield n
        n += 2


def prime_string(upto):
    prime_str = ""
    for prime in primes():
        prime_str += str(prime)
        if len(prime_str) > upto:
            break
    return prime_str


def solution(i):
    return prime_string(i+5)[i:i+5]