def is_prime(number):
    if number <= 1:
        is_prime_ = False
    else:
        is_prime_ = True
        for i in range(2, number):
            remainder_of_number = number % i
            if remainder_of_number == 0:
                is_prime_ = False
                break
        return is_prime_
    return is_prime_

n = int(input("Enter a number: "))
result = is_prime(n)
if result == True:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')
