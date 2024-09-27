


def find_bonus(perf):
    bonus = [1]*len(perf)

    for i in range(len(perf)):
        if i == 0 and i < len(perf)-1:
            bonus[i] = (bonus[i] + 1) if perf[i] > perf[i+1] else bonus[i]
        elif i > 0 and i < len(perf)-1:
            if perf[i] > perf[i+1] and perf[i] > perf[i-1]:
                bonus[i] = (bonus[i] + 2)
            elif perf[i] > perf[i+1] or perf[i] > perf[i-1]:
                bonus[i] = (bonus[i] + 1)
            else:
                bonus[i] = bonus[i]
            
        elif i == len(perf)-1:
            bonus[i] = (bonus[i] + 1) if perf[i] > perf[i-1] else bonus[i]

    return bonus

# Test code
#perf = [1, 2, 3, 2, 3, 5, 1]
perf = [1,2,3,4,5,6,7,8,9,10]
bonus=find_bonus(perf)
print(bonus)
