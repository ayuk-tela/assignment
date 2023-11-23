def calculate_sum(m):
    total = 0
    for i in range(1, m+1):
        total += (i**2 + 1) / (i + 1)
    return total

# Example usage
m = 5
result = calculate_sum(m)
print("The sum for m =", m, "is:", result)
