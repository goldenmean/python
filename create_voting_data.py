import random

# Number of votes to generate

# Range for voter IDs (1-50)
num_of_voters = 30
voter_id_range = range(1, num_of_voters+1)
# Range for candidate IDs (1-4)
candidate_id_range = range(1, 5)

# Create voting.txt with random voting data
with open('voting.txt', 'w') as file:
    # Generate unique voter IDs to ensure no duplicate voting
    voter_ids = random.sample(voter_id_range, num_of_voters)
    
    for voter_id in voter_ids:
        # Randomly select a candidate
        candidate_id = random.choice(candidate_id_range)
        # Write the voting record
        file.write(f"{voter_id}, {candidate_id}\n")