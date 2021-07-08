import random
def generate_key():
 alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 key = []
 while len(alphabet) > 0:
   key.append(alphabet.pop(random.randint(0,len(alphabet) - 1)))
 return key
def rndls(T,K):
  if ord(T)>=ord('a') and ord(T)<=ord('z'):
    return K[ord(T)-ord('a')]
  elif ord(T)>=ord('Z') and ord(T)<=ord('Z'):
    return K[ord(T)-ord('A')].upper()
  else:
    return T
def rndws(T,K):
  w=""
  for l in T:
    w+=rndls(l,K)
  return w
def rndms(T,K):
  m=[]
  for w in T:
    m.append(rndws(w,K))
  return m
def drndls(T,K):
  if ord(T)>=ord('a') and ord(T)<=ord('z'):
    return chr(K.index(T)+ord('a'))
  elif ord(T)>=ord('A') and ord(T)<=ord('Z'):
    return chr(K.index(T.lower())+ord("A")).upper()
  else:
    return T
def drndws(T,K):
  w=""
  for l in T:
    w+=drndls(l,K)
  return w
def drndms(T,K):
  m=[]
  for w in T:
    m.append(drndws(w,K))
  return m