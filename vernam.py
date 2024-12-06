def new_key(key,text):
    if len(key)==len(text/2):
        key+=key
    else:
        diff=len(text)-len(key)
        for i in range(diff):
            key+=key[i]
    return key
            
key=input("Enter key")
choose=int(input('''
1. enter 1 for encrytion
2. enter 2 for decripthion                                  
                 '''))
if choose==1:
    plain=input("enter the plain")
    cipher=""
    if len(key)<len(plain):
        key=new_key(key,plain)
    for i in range(len(plain)):
        if plain[i]==key[i]:
            cipher+="0"
        else:
            cipher+="1"
    print(cipher)                

elif choose==2:
    cipher=input("enter the cipher")
    plain=""
    if len(key)<len(cipher):
        key=new_key(key,cipher)
    for i in range(len(cipher)):
        if cipher[i]==key[i]:
            cipher+="0"
        else:
            cipher+="1"
    print(cipher)
else:
    print("invalid choose")
        
