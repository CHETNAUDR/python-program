#enumerate function i python .
"""a=[678,656,64,34,6
   ,4654]
index=0
for i in a:
    print(i)
    if(index==3):
       print(i,"harry,awsome")
    index=index+1
"""
a=[678,656,64,34,6
   ,4654]
for index,i in enumerate(a):
    print(i)
    
    if(index==3):
       print(i,"harry,awsome")
    
