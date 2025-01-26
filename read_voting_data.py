


with open('voting.txt', 'r') as f:
    number_of_lines = 7
    lines=[next(f, None) for _ in range(number_of_lines)]
    for line in lines:
        line = line.strip()
        voter_id, candidate = line.split(",")    
        print(voter_id, candidate)



    