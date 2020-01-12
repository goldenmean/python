import re

#https://docs.python.org/2/howto/regex.html#using-regular-expressions
#https://docs.python.org/3/library/re.html
#https://www.tutorialspoint.com/python/python_reg_expressions.htm

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'Dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
   print ("search --> searchObj.group(1) : ", searchObj.groups())
   
else:
   print ("Nothing found!!")