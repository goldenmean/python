"""
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
"""


def min_drinks(preferences):
    from collections import defaultdict

    # Create a dictionary to count the number of customers for each drink
    drink_count = defaultdict(int)
    for customer, drinks in preferences.items():
        for drink in drinks:
            drink_count[drink] += 1

    print(drink_count)
    # drink_count is a default dictionary where key is the drink number and value 
    # is total number of customers who prefer that drink

    # Sort drinks by the number of customers who prefer them, in descending order
    sorted_drinks = sorted(drink_count, key=drink_count.get, reverse=True)

    print(f"Sorted drinks: {sorted_drinks}")

    satisfied_customers = set()
    chosen_drinks = []

    for drink in sorted_drinks:
        chosen_drinks.append(drink)
        for customer, drinks in preferences.items():
            if drink in drinks:
                satisfied_customers.add(customer)
        if len(satisfied_customers) == len(preferences):
            break

    return len(chosen_drinks)

# Example usage:
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

print(min_drinks(preferences))  # Output: 2