


def top_3_candidates(chunk_size):
    voter_ids = set()
    votes = dict()
    #print(f"chunk size: {chunk_size}")
    def read_file_chunksize(chunk_size):
        with open('voting.txt') as f:
            while True:
                lines = [next(f, None) for _ in range(chunk_size)]
                #print(f"lines: {lines}")
                if not lines:
                    break
                print(f"lines: {lines}")
                # Process the chunk of lines
                yield lines

    for chunk in read_file_chunksize(chunk_size):
        for line in chunk:            
            voter = None
            candidate = None
            if line:
                line = line.strip()
                #print(f"line: {line}")            
                voter,candidate = line.split(',')  
                
                #breakpoint()
                voter=int(voter.strip())
                candidate=int(candidate.strip())
                #print(f"voter: {voter}, candidate: {candidate}")
                if voter not in voter_ids:
                    voter_ids.add(voter)
                    votes[candidate] = votes.get(candidate, 0) + 1
                    # Sort the dictionary by values in descending order and print top 3 voted candidates
                    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
                    top_3 = sorted_votes[:3]
                    print("Current Top 3 Candidates are:")
                    for c, v in top_3:
                        print(f"Candidate {c}: {v} votes")
                        
                    # if(len(sorted_votes) >= 3):
                    #     print(f"Top 3 candidates are: {sorted_votes[0][0], sorted_votes[1][0], sorted_votes[2][0]} with votes: {sorted_votes[0][1], sorted_votes[1][1], sorted_votes[2][1]}")
                
                else:
                    print(f"\"Fraud Alert\" voter {voter} has already voted")
            else:
                return             
        
        print("-" * 20)

    


no_of_lines = 7
top_3_candidates(no_of_lines)
# no_of_lines = 2
# top_3_candidates(no_of_lines)    
# no_of_lines = 10
# top_3_candidates(no_of_lines)    
# no_of_lines = 1
# top_3_candidates(no_of_lines)    
        

        
    