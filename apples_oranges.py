
# Problem Statement: https://www.hackerrank.com/challenges/apple-and-orange/problem
#Find the apples and oranges that fall on the house

def apples_oranges_on_house(hstart, hend, a, o, m, n, apples, oranges):
    acnt = 0
    ocnt = 0
    for i in range(m):
        if hstart <= apples[i] + a <= hend:
            acnt += 1
    for i in range(n):
        if hstart <= oranges[i] + o <= hend:
            ocnt += 1
    return acnt, ocnt


print(apples_oranges_on_house(7, 10, 4, 12, 3, 3, [2,3,-4], [3,-2,-4]))
print(apples_oranges_on_house(7, 11, 5, 15, 3, 2, [-2,2,1], [5,-6]))