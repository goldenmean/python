'''
You are running a popsicle stand where each popsicle costs $5. Each customer you encountered
pays with either a $5 bill, a $10 bill, or a $20 bill and only buys a single popsicle. 
The customers that come to your stand come in the ordered given by the customers array where
customers[i] represents the bill the ith customer pays with. Starting with $0, return whether
or not you can serve all the given customers while also giving the correct amount of change.
Ex: Given the following customers…
customers = [5, 10], return truecollect $5 from the first customer, pay no change.collet $10 
from the second customer and give back $5 change.
Ex: Given the following customers…
customers = [10], return falsecollect $10 from the first customer and we cannot give back change.
Ex: Given the following customers…
customers = [5,5,5,10,20], return truecollect $5 from the first 3 customers.collet $10 from the 
fourth customer and give back $5 change.collect $20 from the fifth customer and give back $10
change ($10 bill and $5 bill).
'''



def can_serve_all_customers(customers):
    five_dollars = 0
    ten_dollars = 0
    
    for bill in customers:
        if bill == 5:
            five_dollars += 1
        elif bill == 10:
            if five_dollars == 0:
                return False
            five_dollars -= 1
            ten_dollars += 1
        elif bill == 20:
            if ten_dollars > 0 and five_dollars > 0:
                ten_dollars -= 1
                five_dollars -= 1
            elif five_dollars >= 3:
                five_dollars -= 3
            else:
                return False
        else:
            return False  # Invalid bill value

    return True

# Example usage:
customers1 = [5, 10]
print(can_serve_all_customers(customers1))  # Output: True

customers2 = [10]
print(can_serve_all_customers(customers2))  # Output: False

customers3 = [5, 5, 5, 10, 20]
print(can_serve_all_customers(customers3))  # Output: True

customers4 = [5, 5, 20]
print(can_serve_all_customers(customers4))  