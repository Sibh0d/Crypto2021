from Caesar import decrypt_message
from read_write import print_message,read_file
def Print_All_Messages(T):
  for i in range(26):
    print("(Key: "+str(i)+") " + print_message(decrypt_message(T,i)))
def Crack_Cipher(T):
  best=0
  holders=[]
  words = read_file("Words") #brown.words()
  for i in range(26):
    print(i)
    current=0
    a=decrypt_message(T,i)
    for w in a:
      print(w)
      if w in words:
        current+=1
    current=current/len(T)
    print(current)
    if current>best:
      best=current
      holders=[i]
    elif current==best:
      holders.append(i)
  for h in holders:
    print(decrypt_message(T,h))
    print(best)