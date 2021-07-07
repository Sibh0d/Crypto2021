from read_write import read_file
from RandomSubstitution import generate_key, drndms
def Crack_Random(T):
  letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letterd={'a':7.610054159144563, 'b':1.7080960977641995, 'c':3.596722677405916, 'd':3.263435633939731, 'e':12.484377169837522, 'f':1.8191917789195946, 'g':1.944174420219414, 'h':4.568809887515623, 'i':6.790723510623525, 'j':0.20830440216636578, 'k':0.8887654492431607, 'l':3.7633661991390084, 'm':2.5413137064296625, 'n':6.332453825857519, 'o':7.2212192751006805, 'p':2.666296347729482, 'q':0.541591445632551, 'r':7.165671434522983, 's':6.013053742535759, 't':11.012359394528538, 'u':2.94403555061797, 'v':0.8748784890987363, 'w':1.3886960144424385, 'x':0.611026246354673, 'y':1.874739619497292, 'z':0.16664352173309263}
  count={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
  ln=0
  words=T
  key=[]
  for w in words:
    for l in w:
      if l.lower() in letters:
        ln+=1
        count[l.lower()]+=1
  for x in count:
    count[x]=100*count[x]/ln
    print(x, end=" ")
    print(count[x])
  values=sorted(count.values())
  print(values)
  for x in values:
    for y in letters:
      if count[y]==x:
        key.append(letters.pop(letters.index(y)))
  for x in key:
    print(x,end="")
  values=sorted(letterd.values())
  print(values)
  letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  norm=[]
  for x in values:
    for y in letters:
      if letterd[y]==x:
        norm.append(letters.pop(letters.index(y)))
  for x in key:
    print(x,end="")
  print()
  letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for x in norm:
    
  
#    words=read_file("Words")
#    while (True):
#      current=0
#      key=generate_key
#      for x in T:
#        if T in words:
#          current+=1
#      if current/len(T)>.1:
#        print(drndms(T,key))
#        break
  #mp=[]
  #for x in range(26):
  #  for y in range(26):
  #    mp.append([chr(ord("a")+x),chr(ord("a")+y)])
  #for x in mp:
  #  print(x)