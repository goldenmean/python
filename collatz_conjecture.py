


# Starting with a positive integer, run the collatz conjecture sequence

def collatz_conjecture(n):
    
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)


# Example usage

collatz_conjecture(3)
