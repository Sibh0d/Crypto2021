from Caesar import decrypt_message
from read_write import print_message,read_file
def Print_All_Messages(T):
  for i in range(26):
    print("(Key: "+str(i)+") " + print_message(decrypt_message(T,i)))
def Crack_Caesar(T):
  t=[]
  for w in T:
    if w!="\n":
      t.append(w)
  best=0
  holders=[]
  words = read_file("Words") #brown.words()
  for i in range(26):
    print(i)
    current=0
    a=decrypt_message(t,i)
    for w in a:
      print(w,end=" ")
      if w.lower() in words:
        current+=1
    current=current/len(t)
    print()
    print(current)
    if current>best:
      best=current
      holders=[i]
    elif current==best:
      holders.append(i)
  print()
  for h in holders:
    print(print_message(decrypt_message(T,h)))
    print()
  print(best)
  print(holders)