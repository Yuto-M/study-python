memo = {1: 1, 2: 1}
def finbonacci(n):
    if n in memo:
        return memo[n]
    memo[n] = finbonacci(n -2) + finbonacci(n - 1)
    return memo[n]

print(finbonacci(6))