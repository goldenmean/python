
def min_cost_to_build_houses(costs):
    if not costs:
        return 0

    n = len(costs)  # number of houses
    k = len(costs[0])  # number of colors

    # Initialize the previous row with the first row of costs
    prev_row = costs[0]

    # Iterate over each house starting from the second one
    for i in range(1, n):
        current_row = [0] * k
        for j in range(k):
            # Find the minimum cost for the previous row excluding the current column j
            min_cost = float('inf')
            for m in range(k):
                #You can't have the current house in column j of same color as one above it(neighbour)
                if m != j:
                    min_cost = min(min_cost, prev_row[m])
            current_row[j] = costs[i][j] + min_cost
        prev_row = current_row

    # The result is the minimum value in the last processed row
    return min(prev_row)

# Example usage
costs = [
    [1, 5, 3],
    [2, 9, 4],
    [3, 1, 8]
]

print(min_cost_to_build_houses(costs)) 