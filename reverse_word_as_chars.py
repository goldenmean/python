

'''
Reverse the words in the list of characters. Words are separated by a single space
'''

def reverse_words(message):
    r=len(message)
    res=[]
    r=len(message)-1
    end=len(message)

    while r > 0:
        #print(r,end)
        while message[r] != ' ': 
            r -= 1
            if r < 0:
                break

        print(r,end)
        for i in range(r+1,end):
            res.append(message[i])

        end=r
        r-=1 
        print(r,end)       


    for i in range(0,end):
        res.append(message[i])

    return res


def reverse_inplace(message):
    #reverse each character in the list
    message=message[::-1]
    #Then reverse individual words

    l = 0    
    for r in range(len(message)+1):
        if r == len(message) or message[r] == ' ': 
            message[l:r] = message[l:r][::-1]
            l = r+1

    return message


#Test program

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

#print(reverse_words(message))            

print(reverse_inplace(message))