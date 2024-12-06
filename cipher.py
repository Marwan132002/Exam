import string
letters=string.ascii_lowercase
key =int(input("Enter the key :"))
choose=int(input("""
1. Enter 1 for encryption \n
2. Enter 2 for decryption \n
"""))
if choose==1:
    plain=input("Enter plaintext").lower()
    cipher=""
    for char in plain:
        index=letters.find(char)
        if index!=-1:
            index=(index+key)%26
            cipher+=letters[index]
        else:
            cipher+=char
    print(cipher)
elif choose==2:
    cipher=input("Enter the ciphertext").lower()
    plain=""
    for char in cipher:
        index=letters.find(char)
        if index!=-1:
            index=(index-key)%26
            plain+=letters[index]
        else:
            plain+=char
    print(plain)
else:
    print("Wrong Choice!!!!")   
                                 
    