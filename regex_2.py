'''
Python regex examples
'''


import re


r'''
text = "The quick brown fox jumps over the lazy dog"

# looks for first two words separated by a space (\w+)
match = re.match(r"(\w+) (\w+)", text)
if match:
    print(f"{match.group(1)} {match.group(2)} ")

'''

r'''

# Example 3: Phone number validation
text = "Someone Phone 123-456-7890 inside a string"
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", text)
if match:
    print("Phone number format matched")

'''
    
r'''

# Example 4: Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "345test@example-123.au"
match = re.match(email_pattern, email)
if match:
    print("Valid email address")
else:
    print("Invalid email address")

'''

#Multiple matches
text = "One apple, two bananas, three oranges."
fruit_pattern = r"(\w+) (\w+)"
matches = re.findall(fruit_pattern, text)
#print(matches)
for quantity,fruit in matches:
    print(f"{quantity} {fruit}")

