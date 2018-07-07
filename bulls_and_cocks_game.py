import random
n = ''.join(random.sample("0123456789", 4))
n=int(n)
temp=n
print(n)
f=[]
while n>0:
    rem=n%10
    n=n//10
    f.append(rem)
bull=0
while bull<4:
    bull=0
    cock=0
    i=int(input('enter a 4 digit unique number'))
    l=[]
    while i>0:
        rem=i%10
        i=i//10
        l.append(rem)
    r=set(l)
    if(len(r)!=4):
        print("enter only unique number")
        break
    for h in range(4):
        for g in range(4):
            if(l[h]==f[g]):
                cock=cock+1
    for m in range(4):
        if(l[m]==f[m]):
            bull=bull+1
            cock=cock-1
    print("cocks")
    print(cock)
    print("bulls")
    print(bull)
if(bull==4):
    print("yes you gussed it correct, the number is")
    print(temp)
    
        
  
