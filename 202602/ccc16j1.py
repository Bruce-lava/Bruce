G=input()
a=G.count('win')
if a>=5:
    print('1')
if a>=3 and a<=4:
    print('2')
if a>=1 and a<=2:
    print('3')
import sys
sys.stdin=open('in.txt','r')
sys.stdout=open('out.txt','w')
print("hello")