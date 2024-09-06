'''
Generate random characters- alphabets and numbers and punctuations
'''

import random
import string

def generate_random_string(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_characters) for _ in range(length))

random_string = generate_random_string(10)
print(random_string)





def random_unicode_char_from_ranges(ranges):
    range_start, range_end = random.choice(ranges)
    return chr(random.randint(range_start, range_end))

def generate_random_unicode_string(length, ranges):
    return ''.join(random_unicode_char_from_ranges(ranges) for _ in range(length))

# Various chartacter sets 
# https://en.wikipedia.org/wiki/List_of_Unicode_characters#Brahmic_(Indic)_scripts

# Example Unicode ranges: Basic Latin, Latin-1 Supplement, Greek and Coptic, Cyrillic
unicode_ranges = [
    (0x0020, 0x007E),   # Basic Latin
    (0x00A0, 0x00FF),   # Latin-1 Supplement
    (0x0370, 0x03FF),   # Greek and Coptic
    (0x0400, 0x04FF)    # Cyrillic
]

random_unicode_string = generate_random_unicode_string(10, unicode_ranges)
print(random_unicode_string)