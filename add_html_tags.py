'''
I was given a large string with different punctuation in like line breaks, paragraphs
and symbols and was asked to parse this string to insert HTML tags at punctuation points,
like < br > tags and < strong > tags at line breaks and paragraphs respectively.
'''


import re

def insert_html_tags(text):
    # Replace line breaks with <br>
    text = re.sub(r'\n+', '<br>', text)
    
    # Wrap lines in <p> tags
    lines = text.split('\n')
    wrapped_lines = ['<p>' + line.strip() + '</p>\n' for line in lines]
    
    # Join wrapped lines
    text = ''.join(wrapped_lines)
    
    # Wrap strong text in <strong> tags
    #text = re.sub(r'\b(\w+)\b', r'<strong>\1</strong>', text)
    
    return text

# Test the function
input_text = """This is a sample text
with multiple lines
and some strong text"""

result = insert_html_tags(input_text)
print(result)