#Find maximum number of zeros between two ones in a binary representation of given integer
def bin_zero_gap(n):
    br=bin(n)[2:]
    print br
    len=0
    maxgap=0
    for b in br:        
        if b == '1':
            if len > maxgap:
                maxgap=len
                len=0
        else:
            len = len + 1
        
        

    print "maximum zero gap length in binary representation of %d is %d\n" % (n, maxgap)
    
#Find maximum sequence of zeros anywhere in a binary representation of given integer
def bin_zero_seq(n):
    br=bin(n)[2:]
    print br
    len=0
    maxlen=0
    for b in br:        
        if b == '0':
            len = len + 1
            #print "len is %d" % len
            
        else:            
            if len > maxlen:
                maxlen=len
                len=0
                print "maxlen is %d" % maxlen
            continue
        
    if len > maxlen:
        maxlen=len    

    print "maximum zero sequence length in binary representation of %d is %d\n" % (n, maxlen)
    
bin_zero_gap(6416)  
bin_zero_seq(6416)  
    