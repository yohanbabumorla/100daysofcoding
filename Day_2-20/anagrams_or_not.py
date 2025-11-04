def count_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def anagram_or_not(str_1, str_2):
    # Remove spaces and convert to lower case
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    # Remove punctuation and special characters
    str_1 = ''.join(e for e in str_1 if e.isalnum())
    str_2 = ''.join(e for e in str_2 if e.isalnum())

    # Count frequencies
    str1_freq = count_frequencies(str_1)
    str2_freq = count_frequencies(str_2)

    # Check if frequencies match
    return str1_freq == str2_freq

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

res = anagram_or_not(string1, string2)

if res:
    print(f"String 1: {string1} \nString 2: {string2} \nThese are Anagrams")
else:
    print(f"String 1: {string1} \nString 2: {string2} \nThese are Not-Anagrams")
