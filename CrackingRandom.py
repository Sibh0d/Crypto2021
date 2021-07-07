from read_write import read_file
from RandomSubstitution import generate_key,drndm
def Crack_Random(T):
  words=read_file("Words")
  while (True):
    key=generate_key()
    current=0
    for x in T:
      if x in words:
        current+=1
    if current/len(T)>.1:
      print(drndm(T,key))
      break

  #mp=[]
  #for x in range(26):
  #  for y in range(26):
  #    mp.append([chr(ord("a")+x),chr(ord("a")+y)])
  #for x in mp:
  #  print(x)