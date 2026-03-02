a=input()
p=a.count(':-(')
q=a.count(':-)')
if p==q and p>0 and q>0:
    print('unsure')
if p==0 and q==0:
    print('none')
if p>q:
    print('happy')
if q>p:
    print('sad')