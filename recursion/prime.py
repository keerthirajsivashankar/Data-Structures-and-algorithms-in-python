def isprime(n,d=None):
    if n <= 1:
        return False
    if d is None:
        d = int(n ** 0.5)
    if d < 2:
        return True
    if n % d == 0 :
        return False
    return isprime(n,d-1)
n = int(input())
print(isprime(n))