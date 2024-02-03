def countCharacters(words, chars):
    result = []
    for i in words:
        for j in i:
            print(chars.count(j), i.count(j))
            if chars.count(j) < i.count(j):
                break
        else:
            result.append(len(i)) 
    return sum(result)
    
#words = ["cat","bt","hat","tree"]
#chars = "atach"

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

print(countCharacters(words, chars))