from Caesar import encrypt_letter,decrypt_letter
from read_write import print_message
def VigenereM(T,K):
  pos=0
  text=[]
  for w in T:
    word=""
    for l in w: 
      word+=encrypt_letter(l,(ord(K[pos%len(K)])-ord("a")))
      pos+=1
    text.append(word)
  return text
def DVigenereM(T,K):
  pos=0
  text=[]
  for w in T:
    word=""
    for l in w: 
      word+=decrypt_letter(l,(ord(K[pos%len(K)])-ord("a")))
      pos+=1
    text.append(word)
  return text