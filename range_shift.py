

def shift_range(value, p, q, a, b):
    # Ensure the value is within the original range
    if value < p or value > q:
        raise ValueError("Value is outside the original range.")
    
    # Perform the linear transformation
    new_value = a + (value - p) * (b - a) / (q - p)
    return new_value

# Example usage
original_value = 5
p, q = 0, 10
a, b = 20, 30

shifted_value = shift_range(original_value, p, q, a, b)
print(f"The value {original_value} in range [{p}, {q}] shifts to {shifted_value} in range [{a}, {b}].")