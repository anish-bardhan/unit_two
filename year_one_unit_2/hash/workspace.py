import hash

b_hash = hash.binary_hash

def encrypt(message):
    ans = []
    message = list(message)
    for x in message:
        x = b_hash[x]
        ans.append(x)
        word = "-".join(ans)
    print(word)

encrypt("yuxin")

def decrypt(message):
    ans = []
    message = list(message)
    for key,value in b_hash.items(message):
        message = key
        ans.append(message)
        word = "-".join(ans)
    print(word)
encrypt("1101101-1100001-1110010-1101011")
