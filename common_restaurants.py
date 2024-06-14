'''
You and a friend are trying to choose a restaurant to go to. You both give your 
preferences of restaurants in separate lists. You need to find a restaurant to 
go to that's listed in both of your preferences that has the least index sum. 
If there are ties, output all restaurants you could go to together.

Ex: Given the following lists...

list1 = ["A", "B", "C", "D"], list2 = ["D", "B", "C"], return [“B”] (“B” is the 
least index sum 1 + 1 whereas “D” is 3 + 0).
Ex: Given the following lists...

list1 = [“C”], list2 = [“D”], return [].
'''

def find_restaurants(list1, list2):
    res = [("",float("+inf"))]
    for h in list1: 
        if h in list2:
            i = list1.index(h) + list2.index(h)
            if i < res[0][1]:
                res = [(h,i)]
            elif i == res[0][1]:
                res.append((h,i))

    return [i[0] for i in res]


#l1=["A", "B", "C", "D"]; l2=["D", "B", "C"]
l1=["A", "B", "C", "D"]; l2=["B", "A", "X", "Z"]

print(find_restaurants(l1,l2))