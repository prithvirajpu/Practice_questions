#string reverse

st='hello there iam here'
new=''
for i in st:
    new=i+new
print(new)

#Find the frequency of the string 

st='hello there iam here'
new={}
for i in st:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
print(new)

#Frequency-Another method- using get

st='hello there iam here'
new={}
for i in st:
    new[i]=new.get(i,0)+1
print(new)
