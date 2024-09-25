def checkAscii(c):
    banned_chars = " ,;.!:(){}[]\"\'"
    if c not in banned_chars:
        return True
    else:
        return False

def parseTildes(c):
    if c == 'á':
        return 'a'
    if c == 'é':
        return 'e'
    if c == 'í':
        return 'i'
    if c == 'ó':
        return 'o'
    if c == 'ú':
        return 'u'
    return c

alphabet = "abcdefghijklmnñopqrstuvwxyz"
print(alphabet)

key = input("Enter the key:\n")
option = input("Do you want to (C)ipher or (D)ecipher the message?\n")
while option != 'C' and option != 'D':
    option = input("Do you want to (C)ipher or (D)ecipher the message?\n")
result = ""

if option == 'C':
    msg = input("Enter the message that you want to cipher:\n")
    msg = msg.lower()
    cipher_msg = ""
    it = 0
    for c in msg:
        c = parseTildes(c)
        if checkAscii(c):
            cipher_msg = cipher_msg + alphabet[(alphabet.index(c) + alphabet.index(key[it % len(key)])) % len(alphabet)]
            it+=1
        else:
            cipher_msg = cipher_msg + c
    print(cipher_msg)
elif option == 'D':
    msg = input("Enter the message that you want to decipher:\n")
    msg = msg.lower()
    decipher_msg = ""
    it = 0
    for c in msg:
        c = parseTildes(c)
        if checkAscii(c):
            decipher_msg = decipher_msg + alphabet[abs((alphabet.index(c) - alphabet.index(key[it % len(key)]))) % len(alphabet)]
            it+=1
        else:
            decipher_msg = decipher_msg + c
    print(decipher_msg)