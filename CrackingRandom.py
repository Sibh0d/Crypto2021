from read_write import read_file
from RandomSubstitution import drndms
"""def percents(T):
  per={}.setdefault(0)
  tl=0
  for w in T:
    for l in w:
      if ord(l.lower())<=ord('z') and ord(l.lower())>=ord('a'):
        tl+=1
        per[l]+=1
  for x in per:
    per[x]=100*per[x]/tl
  return percents"""
def Crack_Random(T):
  lttrs=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letters=lttrs.copy()
  """letterd={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
  words=read_file("Textforfrequency")
  ln=0
  for w in words:
    for l in w:
      if l.lower() in letters:
        ln+=1
        letterd[l.lower()]+=1
  for x in letterd:
    letterd[x]=100*letterd[x]/ln
    print(x+": "+str(letterd[x]))
  print("\n"*4)"""
  letterd={'a':8.2, 'b':1.5, 'c':2.8, 'd':4.3, 'e':13, 'f':2.2, 'g':2, 'h':6.1, 'i':7, 'j':.15, 'k':.77, 'l':4, 'm':2.4, 'n':6.7, 'o':7.5, 'p':1.9, 'q':.095, 'r':6, 's':6.3, 't':9.1, 'u':2.8, 'v':.98, 'w':2.4, 'x':.15, 'y':2, 'z':.074}
  count={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
  words=T
  ln=0
  key=[]
  for w in words:
    for l in w:
      if l.lower() in letters:
        ln+=1
        count[l.lower()]+=1
  for x in count:
    count[x]=100*count[x]/ln
    print(x+": "+str(count[x]))
  values=sorted(count.values())
  for x in values:
    for y in letters:
      if count[y]==x:
        key.append(letters.pop(letters.index(y)))
  values=sorted(letterd.values())
  letters=lttrs.copy()
  norm=[]
  for x in values:
    for y in letters:
      if letterd[y]==x:
        norm.append(letters.pop(letters.index(y)))
  letters=lttrs.copy()
  this=[]
  for x in norm:
    this.append(0)
  for x in letters:
    this[letters.index(x)]=key[norm.index(x)]
  return [drndms(T,this),this]