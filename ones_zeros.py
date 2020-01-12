def stringy(size):
    # Good Luck!
    zeros = [0] * ((size+1)/2)
    ones = [1] * ((size+1)/2)
    final = []
    for i in xrange(0,((size+1)/2)):
        final.append(ones[i])   
        final.append(zeros[i])
   
       
    if size%2 == 0:
        my1 = str(final[:size]).strip('[]')
        my2 = my1.replace(',','')
        my3=my2.replace(' ','')
        return my3
    elif size%2 == 1:
        my1 = str(final[:-1]).strip('[]')
        my2 = my1.replace(',','')
        my3=my2.replace(' ','')
        return my3
	
test.describe("Basic Tests")

test.it("Should be a string")
test.assert_equals(str(type(stringy(5)))[1:-1],"type 'str'","stringy() should return a string")

test.it("Should start with '1'")
test.assert_equals(stringy(10)[0],'1',"Whoops your string doesn't start with a '1'")

test.it("Should have the correct length")
for i in xrange(1,5):
  test.assert_equals(len(stringy(i)),i,"Make sure your string is the right length")

test.it("Should work for some simple tests")
test.assert_equals(stringy(3), '101', 'oops try again')
test.assert_equals(stringy(5), '10101', 'oops try again')
test.assert_equals(stringy(12), '101010101010', 'oops try again')
test.assert_equals(stringy(26), '10101010101010101010101010', 'oops try again')
test.assert_equals(stringy(28), '1010101010101010101010101010', 'oops try again')	