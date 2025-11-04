def reversed_s(string):
    string_len = len(string)
    reversed_string = ''
    for i in range(string_len-1, -1, -1):
        reversed_string += string[i]
    return reversed_string


s = input('')
s = s.upper()
print(f'The Original string: {s}')
reversed_string = reversed_s(s)
print(f'the reversed string {reversed_string}')