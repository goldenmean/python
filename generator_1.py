


def infinite_sequence(num=0):
    #num = 0
    while True:
        yield num       
        num += 1


g = infinite_sequence()
print(next(g))
print(next(g))
#g.send(555)
#g.send(666) 
print(next(g))
print(next(g))

print("--------")




#def generator_with_send(value=22):
def generator_with_send(value=None):
    while True:
        value = yield value
        print(f"Received value: {value}")


g = generator_with_send()
print(next(g))
print(g.send(555))
print(next(g))
x=g.send(666)
print(x)

#g.send(666)
#print(next(g))
#g.send(777)
#print(next(g))

