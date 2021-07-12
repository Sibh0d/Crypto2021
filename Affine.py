def AEL(P,K):
  if ord(P)>=ord("a") and ord(P)<=ord("z"):
    return chr((K[0]*(ord(P)-ord("a"))+K[1])%26+ord("a"))
  elif ord(P)>=ord("A") and ord(P)<=ord("Z"):
    return chr((K[0]*(ord(P)-ord("A"))+K[1])%26+ord("A"))
  else:
    return P
def AEW(P,K):
  w=""
  for l in P:
    w+=AEL(l,K)
  return w
def AEM(P,K):
  m=[]
  for w in P:
    m.append(AEW(w,K))
  return m
def ADL(C,K):
  inverse=1
  while True:
    if (inverse*K[0])%26==1:
      break
    else:
      inverse+=1
  if ord(C)>=ord("a") and ord(C)<=ord("z"):
    return chr(inverse*(ord(C)-ord("a")-K[1])%26+ord("a"))
  elif ord(C)>=ord("A") and ord(C)<=ord("Z"):
    return chr(inverse*(ord(C)-ord("A")-K[1])%26+ord("A"))
  else:
    return C
def ADW(C,K):
  w=""
  for l in C:
    w+=ADL(l,K)
  return w
def ADM(C,K):
  m=[]
  for w in C:
    m.append(ADW(w,K))
  return m