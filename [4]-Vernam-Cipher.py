def ENCRYPT(PlainText,KEY):
    RESULT=""
    for i in range(len(PlainText)):
        j=i%len(KEY)
        RESULT+=chr(ord(PlainText[i])^ord(KEY[j]))
    return RESULT

def DECRYPT(PlainText,KEY):
    RESULT=""
    for i in range(len(PlainText)):
        j=i%len(KEY)
        RESULT+=chr(ord(PlainText[i])^ord(KEY[j]))
    return RESULT

print(ENCRYPT("Vineet","Hello"))
print(DECRYPT(ENCRYPT("Vineet","Hello"),"Hello"))
