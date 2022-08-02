import string
alphabet = list(string.ascii_lowercase)

messageStandart = input()
messageStandart = messageStandart.lower()

messageSecret = ""
for i in messageStandart:
    if i == " ":
        messageSecret += " "
    elif i in alphabet:
        a = alphabet.index(i)
        messageSecret += alphabet[-a-1]

print(messageSecret)

