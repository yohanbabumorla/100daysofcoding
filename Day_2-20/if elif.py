name = input("Enter the name: ")
rule = len(name)
if rule < 3:
    print("sorry!.. name must be at least 3 characters")
elif rule >50:
    print("name not exceed 50 characters")
else:
    print("looks good")
