def encrypt_letter(P,K):
  if ord(P)>=ord("a") and ord(P)<=ord("z"):
    return chr((ord(P)-ord("a")+K)%26+ord("a"))
  elif ord(P)>=ord("A") and ord(P)<=ord("Z"):
    return chr((ord(P)-ord("A")+K)%26+ord("A"))
  else:
    return P
def encrypt_word(P,K):
  w=""
  for l in P:
    w+=encrypt_letter(l,K)
  return w
def encrypt_message(P,K):
  m=[]
  for w in P:
    m.append(encrypt_word(w,K))
  return m
def decrypt_letter(C,K):
  if ord(C)>=ord("a") and ord(C)<=ord("z"):
    return chr((ord(C)-ord("a")-K)%26+ord("a"))
  elif ord(C)>=ord("A") and ord(C)<=ord("Z"):
    return chr((ord(C)-ord("A")-K)%26+ord("A"))
  else:
    return C
def decrypt_word(C,K):
  w=""
  for l in C:
    w+=decrypt_letter(l,K)
  return w
def decrypt_message(C,K):
  m=[]
  for w in C:
    m.append(decrypt_word(w,K))
  return m