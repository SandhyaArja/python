 s="sandhya"
for i in range(1,len(s)+1):
    print(s[:i])


s=input()
l=len(s)
word=""
for i in range(l):
    if i%2==0:
        word+=s[i].upper()
        
    else:
        word+=s[i].lower()
print(word)

def find(n,char):
    count=0 
    for i in n:
        if i in char:
            count+=1 
    print(str(char),count)
n=input()
print(find(n,"a"))



s=input()
all_freq={}
for i in s:
    if i in all_freq:
        all_freq[i]+=1 
    else:
        all_freq[i]=1 
print(str(all_freq))
            
def reverse(s):
    if len(s)==0:
        return s 
    else:
        return reverse(s[1:])+s[0]
s="sandhya"
rev=reverse(s)
print((rev))



a=int(input())
b=int(input())
x=lambda a,b:a*b 
print(x(a,b))
m=lambda a:a*a*a 
print(m(a))




