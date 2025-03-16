class VoteStream:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.voter_ids = set()
        self.votes = {}
        
    def get_next_vote(self):
        """Process next vote from stream and return top 3 candidates"""
        line = self.file.readline() #read 1 line at a time simulating the stream
        if line:
            line = line.strip()
            voter, candidate = line.split(',')
            
            voter = int(voter.strip())
            candidate = int(candidate.strip())
            
            if voter not in self.voter_ids:
                self.voter_ids.add(voter)
                self.votes[candidate] = self.votes.get(candidate, 0) + 1
                return self.get_top_3(), None
            else:
                return None, f"Fraud Alert: Voter {voter} has already voted"
        return None, "End of stream"
    
    def get_top_3(self):
        sorted_votes = sorted(self.votes.items(), key=lambda x: x[1], reverse=True)
        return sorted_votes[:3]
    
    def close(self):
        self.file.close()

# Example usage
if __name__ == "__main__":
    vote_stream = VoteStream("voting.txt")
    
    while True:
        top_3, fraud_alert = vote_stream.get_next_vote()
        if fraud_alert == "End of stream":
            break
        if fraud_alert:
            print(fraud_alert)
        if top_3:
            print("Current Top 3 Candidates:")
            for candidate, votes in top_3:
                print(f"Candidate {candidate}: {votes} votes")
        print("-" * 30)
    
    vote_stream.close()