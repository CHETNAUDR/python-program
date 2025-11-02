import string
import random
s1=string.ascii_uppercase
print(s1)
s2=string.ascii_lowercase
print(s2)
s3=string.digits
print(s3)
s4=string.punctuation
print(s4)
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print(s)
n=int(input("enter the length of password"))
print(s[0:n])
print("".join(s[0:n]))# join function ek list ke elemet ko merge karne ka kam  kar rahi hai
# print("".join(random.sample(s,n))# yaha pr suffle wl kam nhi karna nhi padega direct sample function use karte h
