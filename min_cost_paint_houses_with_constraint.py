'''
You are tasked with painting a row of houses in your neighborhood such that each house is painted
either red, blue, or green. The cost of painting the ith house red, blue or green, is given by 
costs[i][0], costs[i][1], and costs[i][2] respectively. Given that you are required to paint each 
house and no two adjacent houses may be the same color, return the minimum cost to paint all the houses.

Ex: Given the following costs array…

costs = [[1, 3, 5],[2, 4, 6],[5, 4, 3]], return 8.
Paint the first house red, paint the second house blue, and paint the third house green.
'''

def min_cost_to_paint_houses(costs):
    if not costs:
        return 0

    n = len(costs)
    # Initialize the first house's costs
    prev_red, prev_blue, prev_green = costs[0]

    # Iterate over the rest of the houses
    for i in range(1, n):
        #find cost of painting current house with red, if previous house was painted with blue or green
        current_red = costs[i][0] + min(prev_blue, prev_green)
        #find cost of painting current house with blue, if previous house was painted with red or green
        current_blue = costs[i][1] + min(prev_red, prev_green)
        #find cost of painting current house with green, if previous house was painted with red or blue
        current_green = costs[i][2] + min(prev_red, prev_blue)

        # Update the previous costs for the next iteration
        prev_red, prev_blue, prev_green = current_red, current_blue, current_green

    # The answer will be the minimum cost of painting the last house any color
    return min(prev_red, prev_blue, prev_green)

# Example usage
costs = [[1, 3, 5], [2, 4, 6], [5, 4, 3]]
print(f"The minimum cost to paint all houses is {min_cost_to_paint_houses(costs)}")