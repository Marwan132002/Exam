import string 
letters=string.ascii_lowercase+" "
key=input("Enter the key").lower()
choose=int(input("""
1. enter 1 for encrypt
2. enter 2 for decript
                 """))
if choose==1:
    plain=input("enter the palin").lower()
    cipher=""
    for i in range(len(plain)):
        index_p=letters.index(plain[i])
        index_k=letters.index(key[i])
        if index_p!=-1:
            index=(index_p+index_k)%27
            cipher+=letters[index]
        else:
            cipher+=plain[i]
    print(cipher)
elif choose==2:
      cipher=input("enter the cipher").lower()
      plain=""
      for i in range(len(cipher)):
          index_c=letters.index(cipher[i])
          index_k=letters.index(key[i])
          if index_c!=-1:
              index=(index_c-index_k)%27
              plain+=letters[index]
          else:
              plain+=cipher[i]
    
      print(plain)
      
    
    
        