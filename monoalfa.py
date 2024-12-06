import string
letters=string.ascii_lowercase
key=input("Enter key").lower()
choose=int(input('''
1. enter 1 for encrytion
2. enter 2 for decripthion                                  
                 '''))
if choose==1:
    plain=input("enter the plain").lower()
    cipher=""
    for char in plain:
        index=letters.index(char)
        if index!=-1:
            cipher+=key[index]
        else:
            cipher+=char
    print(cipher)
elif choose==2:
    cipher=input("enter the cipher").lower()
    plain=""
    for char in cipher:
        index=key.index(char)
        if index!=-1:
            plain+=letters[index]
        else:
            plain+=char
    print(plain)
else:
    print("invalid choose")
        
