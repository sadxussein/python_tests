from itertools import product

# Read the count of the lines and M
lines_count, m = map(int, input().split())

# Store the lines in "data" array
data = [list(map(int, input().split()))[1:] for _ in range(lines_count)]

# Create all possible combinations using "itertools.product"
combs = product(*data)

# Calculate the results and store them in the "results" array
results = [sum(i ** 2 for i in comb) % m for comb in combs]

# Print the maximum result
print(max(results))