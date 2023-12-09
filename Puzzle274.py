"""

Isolated conundrum #274

Positive single digit integers a,b,c and d are such that.

a+1/(b+1/(c+1/d))=20/13

"""

for a in range(1,10):
    for b in range(1,10):    
        for c in range(1,10):
            for d in range(1,10):
                #print(f"{d}")
                ans = a+1/(b+1/(c+1/(d)))
                #print(f"{a},{b},{c},{d} ans = {ans}")
                if round(ans,8) == round(20/13,8):
                    print(f"a is {a}, b is {b}, c is {c}, d is {d}")
