"""
> 5
*****
****
***
**
*
"""
n = int(input("> "))
for i in range( n, 0, -1): #here the value of i starts from n and gradually decrees by 1 until before i reaches 1
    print("*" * i)
print(n)