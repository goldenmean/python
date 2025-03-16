

import unicodedata

def print_unicode_table(start=0x0000, end=0x300):
    for codepoint in range(start, end + 1):
        char = chr(codepoint)
        name = unicodedata.name(char, 'UNKNOWN')
        print(f"U+{codepoint:04X} {char} {name}")

# Print Unicode table for Basic Multilingual Plane (U+0000 to U+FFFF)
#print_unicode_table()


print('\u267A')

print(chr(0x263A))

print(chr(0x267A))


