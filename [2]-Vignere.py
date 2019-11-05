def Encrypt(PlainText,KEY):
    Result=''
    for i in range(len(PlainText)):
        j=i%len(KEY)
        if(PlainText[i].isupper()):
            Result+=chr(((ord(PlainText[i])+ord(KEY[j]))%26+66))
        else:
            Result+=chr(((ord(PlainText[i])+ord(KEY[j]))%26+98))
    return Result

print(Encrypt("VINeeT","WOW"))

    

