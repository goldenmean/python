





def find_destination_city(flights):
    #create a dictionary from the flights for quick search using starting city as key and 
    # arrival city as value of the dictionary
    flight_dict = {}
    for flight in flights:
        flight_dict[flight[0]] = flight[1]
    
    for k,v in flight_dict.items():
        #if v not in flight_dict.keys():
        #Find the arrival city that is not in the dictionary of starting city keys
        if v not in flight_dict:
            return v
    


flights = [["A", "B"], ["C", "D"], ["B", "C"]]
#flights = [["A", "B"], ["B", "C"]]
print(find_destination_city(flights))

## Solution using set
def final_destination_city(flights):
    outgoing = set()
    
    # Add all departing cities to the outgoing set
    for flight in flights:
        outgoing.add(flight[0])
    
    # Find the arrival city that is not in the outgoing set
    for flight in flights:
        if flight[1] not in outgoing:
            return flight[1]