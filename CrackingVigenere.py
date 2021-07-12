from Caesar import decrypt_letter
from Vigenere import DVigenereM
def average(V):
  total=0
  for x in V:
    total+=x
  return total/len(V)
def getIOC(T):
  count={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
  ln=0
  sm=0
  for w in T:
    for l in w:
      if ord(l.lower())<=ord("z") and ord(l.lower())>=ord("a"):
        count[l.lower()]+=1
        ln+=1
  if ln<1000:
    for x in count:
      if count[x]!=0:
        count[x]=(count[x]/ln)*((count[x]-1)/(ln-1))
      sm+=count[x]
  else:
    for x in count:
      count[x]=(count[x]/ln)**2
      sm+=count[x]
  return sm
def getKeyLen(T):
  lows=[]
  holders=[]
  low=1
  avgs=0
  for i in range(1,len(T)):
    sub=[]
    for x in range(i):
      sub.append("")
    pos=0
    for w in T:
      for l in w:
        if ord(l.lower())>=ord('a') and ord(l.lower())<=ord('z'):
          pos+=1
        sub[pos%(i)]+=l
    print(i)
    print(sub)
    #mean=average(getIOC(sub))
    avg=0
    ln=0
    for x in sub:
      ln+=1
      print(getIOC(x))
      #if getIOC(x)>0:
      avg+=abs(getIOC(x))
    avg=avg/ln
    avgs+=avg
    lows.append(str(i)+": "+str(avg))
    if abs(avg-0.06940560771246032)==low:
      holders.append(i)
    elif abs(avg-0.06940560771246032)<low:
      low=abs(avg-0.06940560771246032)
      holders=[i]
    print()
    print(avg)
    print()
  avgs/=len(T)
  print(lows) 
  print()
  print(avgs)
  return holders
def Crack_Vigenere(T,L):
  pos=0