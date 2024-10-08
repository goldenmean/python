"""
Given a string consisting of parentheses, single digits, and positive and 
negative signs, convert the string into a mathematical expression to obtain
the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4
"""

def evaluate_expression(expression):
    def parse(tokens):
        def parse_expression():
            result = parse_term()
            while tokens and tokens[0] in ('+', '-', '*', '/'):
                operator = tokens.pop(0)
                if operator == '+':
                    result += parse_term()
                elif operator == '-':
                    result -= parse_term()
                elif operator == '*':
                    result *= parse_term()
                elif operator == '/':
                    result /= parse_term()

            return result

        def parse_term():
            if tokens[0] == '(':
                tokens.pop(0)  # Remove opening parenthesis
                result = parse_expression()
                tokens.pop(0)  # Remove closing parenthesis
                return result
            else:
                return parse_number()

        def parse_number():
            result = 0
            sign = 1
            if tokens[0] == '-':
                sign = -1
                tokens.pop(0)
            while tokens and tokens[0].isdigit():
                result = result * 10 + int(tokens.pop(0))
            return sign * result

        return parse_expression()

    # Remove spaces and split the expression into tokens
    tokens = [char for char in expression if char != ' ']
    return parse(tokens)

# Test the function
#print(evaluate_expression("1 + (2 + 3)"))  # Should output 4
#print(evaluate_expression("5 - (3 + 1) + 2"))  # Should output 3
#print(evaluate_expression("(-3 + (4 - 1)) * 2"))  # Should output 0
print(evaluate_expression("5 * ((3 + 1) / 4)"))  