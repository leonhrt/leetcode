def kthFactor(n: int, k: int) -> int:
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    
    if len(factors) < k:
        return -1
    
    return factors[k-1]

n = 4
k = 4

print(kthFactor(n, k))
