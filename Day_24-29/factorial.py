def find_factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i
    return result


n = int(input("Enter the number to calculate the factorial of the number: "))
res = find_factorial(n)
print(f'the factorial for the {n} is {res}')