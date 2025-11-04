message = input("> ")
word = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😔"
}
converted_msg = ""
for msg in word:
    converted_msg += emojis.get(msg, msg) +" "
print(converted_msg)