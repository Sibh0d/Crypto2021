def read_file(location):
  file=open(location,"r")
  words=[]
  lines = file.readlines()
  for l in lines:
    words.extend(l.split())
    #words[-1]+="\n"
    words.append("\n")
  return words
def write_file(location,list_of_words):
  file=open(location,"w")
  for w in list_of_words:
    #if w[-2:]!="\n":
    if w !="\n":
      file.write(w+" ")
    else:
      file.write(w)
    #else:
    #  file.write(w)