phone = input("phone: ")
inwords = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += inwords.get(ch, "!") + " "
print(output)