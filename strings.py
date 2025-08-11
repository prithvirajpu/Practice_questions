# String compression

s = "aaabbcccc"
res = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
res += s[-1] + str(count)
print(res)  

# Rotation checking

s1, s2 = "abcde", "deabc"
print(len(s1) == len(s2) and s2 in s1+s1) 

# Anagram methods
# First create frequency dictionries for both string and the check is it same - or use sorted inbuilt function
st='madam'
st1='daamm'
new={}
new1={}
for i in st:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
for i in st1:
    if i in new1:
        new1[i]+=1
    else:
        new1[i]=1
if new1==new:  
    print('anagram')
else:
    print('Not anagram')

# sorted method

print(sorted(st)==sorted(st1))

# Vowels checking

count=0
st='hello there iam here'
for i in st.lower():
    if i in 'aeiou':
        count+=1
print("The count of vowels is :" ,count)

# First non repeating character in the string

st='hello there iam here'
new={}
for i in st:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
for i, j in new.items():
    if j==1:
        print('The first non repeating character is :',i)
        break

# Another method for first non repeating character 
st='hello there iam here'
for i in st:
    if st.count(i)==1:
        print("The first non repeating charater is :",i)
        break

# string reverse

st='hello there iam here'
new=''
for i in st:
    new=i+new
print(new)

# some another methods-slicing 
print(st[::-1])

# Find the frequency of the string 

st='hello there iam here'
new={}
for i in st:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
print(new)

# Frequency-Another method- using get

st='hello there iam here'
new={}
for i in st:
    new[i]=new.get(i,0)+1
print(new)
