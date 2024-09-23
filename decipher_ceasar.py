def checkAscii(c):
    banned_chars = " ,;.!:"
    if c not in banned_chars:
        return True
    else:
        return False

import string
alphabet = "abcdefghijklmnñopqrstuvwxyz"
print(alphabet)
# print(alphabet[13])
shift = int(input("Enter shift amount: "))
r_shift = shift % len(alphabet)
# print(f"Right shift is: {r_shift}")
l_shift = -shift % len(alphabet)
# print(f"Left shift is: {l_shift}")
r_sol =  alphabet[r_shift:] + alphabet[:r_shift]
l_sol =  alphabet[l_shift:] + alphabet[:l_shift]
print(alphabet)
print(r_sol)
msg = "Xbf cqxusebf dhq noqotnz n xnf eqpqf JXNZ fuz cebgqooubz fbz yhotbf. Qx genruob uznxnyñeuob fq eqsufgen rnouxyqzgq."
msg = msg.lower()
decipher_msg = ""
for c in msg:
    if checkAscii(c):
        decipher_msg = decipher_msg + alphabet[r_sol.index(c)]
    else:
        decipher_msg = decipher_msg + c
print(decipher_msg)
