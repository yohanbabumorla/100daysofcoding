pal=input("Enter the string to check Palindrome or Not: ")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome(pal))