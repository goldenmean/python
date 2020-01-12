def soccerCheer(S):
    sa=0
    sb=0
    ch=0
    for g in S:
        if g == 'A':
            sa = sa + 1
            if sa > sb and abs(sa - sb) == 1:
                ch = ch + 1
        elif g=='B':
            sb = sb + 1
            
    return ch
    
    

print soccerCheer("ABBAAA")
print soccerCheer("AAAA")