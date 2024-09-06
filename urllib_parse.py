'''
parse a URL using urllib.parse
'''


from urllib.parse import urlparse, parse_qs

# Sample URL
url = "https://www.example.com/path/to/page?key1=value1&key2=value2#fragment"

# Parse the URL
parsed_url = urlparse(url)

print("Scheme:", parsed_url.scheme)
print("Netloc:", parsed_url.netloc)
print("Path:", parsed_url.path)
print("Query:", parsed_url.query)
print("Fragment:", parsed_url.fragment)

# Parse query parameters
query_params = parse_qs(parsed_url.query)

print("\nParsed Query Parameters:")
for key, values in query_params.items():
    print(f"{key}: {values}")