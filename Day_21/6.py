'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    '''
n = int(input(">Enter odd number: "))
if n % 2 == 0:
    print("Please enter an odd number for a symmetric pyramid.")
else:
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    for j in range(n-2 , -1 ,-1):
        spaces1 = n - j - 1
        stars1 = 2 * j + 1
        print(" " * spaces1 + "*" * stars1)