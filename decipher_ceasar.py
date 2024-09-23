def checkAscii(c):
    banned_chars = " ,;.!:"
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
# print(alphabet)
# print(alphabet[13])
shift = int(input("Enter shift amount:\n"))
r_shift = shift % len(alphabet)
# print(f"Right shift is: {r_shift}")
l_shift = -shift % len(alphabet)
# print(f"Left shift is: {l_shift}")
r_sol =  alphabet[r_shift:] + alphabet[:r_shift]
l_sol =  alphabet[l_shift:] + alphabet[:l_shift]
print("These are the guides to ceaser:\n")
print(alphabet)
print(r_sol)

option = input("Do you to (C)ipher or (D)ecipher? Default is cipher\n")
option = option.upper()
while option != 'D' and option != 'C':
    option = input("Do you to (C)ipher or (D)ecipher? Default is cipher\n")
    option = option.upper()

if option == 'D':
    msg = input("Enter the message you want to decipher:\n")
    msg = msg.lower()
    decipher_msg = ""
    for c in msg:
        if checkAscii(c):
            decipher_msg = decipher_msg + alphabet[r_sol.index(c)]
        else:
            decipher_msg = decipher_msg + c
    print(decipher_msg)
elif option == 'C':
    msg = input("Enter the message you want to cipher:\n")
    msg = msg.lower()
    cipher_msg = ""
    for c in msg:
        c = parseTildes(c)
        if checkAscii(c):
            cipher_msg = cipher_msg + alphabet[r_sol.index(c)]
        else:
            cipher_msg = cipher_msg + c
    print(cipher_msg)