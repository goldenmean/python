print('<table>',*['<tr>'+''.join('<td width=50 height=50 bgcolor=#%03x>'%dict(r=3840,o=3984,y=4080,g=96,b=15,p=1799)[c]for c in r)for r in input().split(',')])



I=raw_input().split(",")
h="<table>"
c=dict(r=3840,o=3984,y=4080,g=96,b=15,p=1799)
for r in I:
 h+="<tr>"
 for x in r:h+="<td width=50 height=50 bgcolor='#%03x'>"%c[x]
print h


