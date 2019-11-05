def ENCRYPT(PlainText,Shift):
    Temp=""
    for i in range(len(PlainText)):
        CHAR=PlainText[i]
        if(CHAR.isupper()):
            Temp+=chr((ord(CHAR)+Shift-65)%26 + 65)
        else:
            Temp+=chr((ord(CHAR)+Shift-97)%26 + 97)
    return Temp

PlainText="Vineet"
Shift=4

print("ENCRYPTED TEXT: " + ENCRYPT(PlainText,Shift))
