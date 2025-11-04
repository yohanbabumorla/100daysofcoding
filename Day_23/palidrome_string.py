def is_palindrome(string):
    string = str(string)
    is_palindrome_ = False
    rev_string = string[::-1]
    if rev_string == string:
        is_palindrome_ = True
    return is_palindrome_


s = input("> ")
result = is_palindrome(s)
if result == True:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")