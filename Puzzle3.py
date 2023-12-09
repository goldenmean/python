import random

a = []
b = [0]*4
rlist = []
suma = 0
sumb = 99

while suma != sumb:
    rlist = [i for i in range(2,9)]
    random.shuffle(rlist)
    b[0] = rlist[4]
    a[::] = rlist[0:4]
    b[1] = a[1] 
    b[2::] = rlist[5::]
    suma = sum(a)
    sumb = sum(b)
    if suma == sumb:
        print(f" Sum is equal suma = %d , sumb = %d, Common element is a[1] = %d, b[1] = %d" %(suma, sumb, a[1] , b[1]) )
        print(a)
        print(b)
        suma = 0
        
    # else:
        # #print("sums different suma = %d, sumb = %d", suma, sumb)