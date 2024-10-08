


def equilibrium_index(arr):
    tot = sum(arr)
    leftsum = 0
    equilibrium_index = []

    for i in range(len(arr)):
        tot = tot - arr[i]
        if leftsum == tot:
            equilibrium_index.append(i)
        leftsum += arr[i]

    return equilibrium_index if len(equilibrium_index) > 0 else -1

#arr = [-7, 1, 5, 2, -4, 3, 0]
#arr = [1, 2, 5, 2, 1]
arr = [3, 1, 9, 2]
print(equilibrium_index(arr))



