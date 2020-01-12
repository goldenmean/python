def dividing_digits(N):
    cnt=0
    num=N

    while N!= 0:
        digit = N%10
        if digit != 0:
            if num % digit == 0:
                cnt = cnt + 1
            N = N/10
        else:
            N=N/10

    return cnt




print dividing_digits(58)
