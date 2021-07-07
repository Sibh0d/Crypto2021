import random
def generate_key():
 alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 key = []
 while len(alphabet) > 0:
   key.append(alphabet.pop(random.randint(0,len(alphabet) - 1)))
 return key
def rndl(T,K):
  if T.islower():
    return K[ord(T)-ord('a')]
  elif T.isupper():
    return K[ord(T)-ord('A')].upper()
  else:
    return T
def rndw(T,K):
  w=""
  for l in T:
    w+=rndl(l,K)
  return w
def rndm(T,K):
  m=[]
  for w in T:
    m.append(rndw(w,K))
  return m
def drndl(T,K):
  if T.islower():
    return chr(K.index(T)+ord('a'))
  elif T.isupper():
    return chr(K.index(T.lower())+ord("A")).upper()
  else:
    return T
def drndw(T,K):
  w=""
  for l in T:
    w+=drndl(l,K)
  return w
def drndm(T,K):
  m=[]
  for w in T:
    m.append(drndw(w,K))
  return m