



def create_dict(a, b):
    return dict(zip(a, b))


a =['a', 'b', 'c']
b=[0, 1, 2]

d = create_dict(a, b)

for k,v in d.items():
    print((k,v))

def create_new_list(a, b):
    return list(zip(a, b))

nl = create_new_list(a, b)
print(nl)
