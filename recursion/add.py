def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1) if b > 0 else recursive_sum(a - 1, b + 1)

# Example Usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", recursive_sum(x, y))
