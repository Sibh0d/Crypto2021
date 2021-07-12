from Affine import ADM
from read_write import read_file
def CrackAffine(T):
  a=0
  t=[]
  for w in T:
    if w!="\n":
      t.append(w)
  high=0
  holders=[]
  words = read_file("Words")
  while True:
    for b in range(26):
      message=ADM(t,[a,b])
      nm=0
      for w in message:
        if w in words:
          nm+=1
      nm/=len(message)
      if nm>high:
        holders=[[a,b]]
      elif nm==high:
        holders.append([a,b])
    if high>=.1:
      return [ADM(T,[a,b]),a,b]