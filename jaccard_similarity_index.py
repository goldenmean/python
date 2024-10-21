"""
You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
"""
#This solution uses Jaccard similarity index between 2 sets A and B 
# len(A&B) / len(A|B) ; intersection divided by union

from collections import defaultdict
from itertools import combinations
from typing import List, Tuple

def calculate_similarity(users1, users2):
    intersection = len(users1 & users2)
    union = len(users1 | users2)
    return intersection / union # jaccard similarity index

def find_top_k_similar_websites(pairs: List[Tuple[str, int]], k: int) -> List[Tuple[str, str]]:
    # Step 1: Create a dictionary of websites to sets of users
    website_users = defaultdict(set)
    for website, user in pairs:
        website_users[website].add(user)
    
    # Step 2: Calculate the similarity for each pair of websites
    similarities = []
    for (website1, users1), (website2, users2) in combinations(website_users.items(), 2):
        similarity = calculate_similarity(users1, users2)
        similarities.append((similarity, (website1, website2)))
    
    # Step 3: Sort the pairs by similarity in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])
    print(similarities[:])
    
    # Step 4: Return the top k pairs
    return [pair for similarity, pair in similarities[:k]]

# Example usage
pairs = [
    ('a', 1), ('a', 3), ('a', 5),
    ('b', 2), ('b', 6),
    ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
    ('d', 4), ('d', 5), ('d', 6), ('d', 7),
    ('e', 1), ('e', 3), ('e', 5), ('e', 6)
]
k = 1
print(find_top_k_similar_websites(pairs, k))  # Output: [('a', 'e')]