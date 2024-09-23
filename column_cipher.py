def checkAscii(c):
    banned_chars = " ,;.!:"
    if c not in banned_chars:
        return True
    else:
        return False
    
if __name__ == "__main__":
    msg = input()
    temp = ""
    for c in msg:
        if checkAscii(c):
            temp += c
    print(temp)
    key = list("tokens")
    # print(key)
    thing = [{x:[]} for x in key]
    it = 0
    for c in msg:
        if checkAscii(c):
            pos = it % len(key)
            thing[pos][key[pos]].append(c.lower())
            it+=1
    key = sorted(key)
    # print(key)
    thing = sorted(thing, key= lambda x: (ord(list(x.keys())[0])-97) )
    # print(thing)

    ans = ""
    for t in thing:
        for key, value in t.items():
            temp = ''.join(value)
            ans = ans + temp
    print(ans)