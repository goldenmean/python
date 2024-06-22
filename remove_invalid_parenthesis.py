


def removeInvalidParentheses(s):
    def isValid(string):
        balance = 0
        for char in string:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    level = {s}
    while True:
        valid = list(filter(isValid, level))
        if valid:
            return valid
        next_level = set()
        for item in level:
            for i in range(len(item)):
                if item[i] in "()":
                    next_level.add(item[:i] + item[i+1:])
        level = next_level

# Example usage:
s = "()())()"
print(removeInvalidParentheses(s))  # Output should be ["(())()", "()()()"]

