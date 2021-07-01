def read_file(location):
  file=open(location,"r")
  words=[]
  lines = file.readlines()
  for l in lines:
    words.extend(l.split())
  return words
def write_file(location,list_of_words):
  file=open(location,"w")
  for w in list_of_words:
    file.write(w+" ")
print(read_file("Poem"))
write_file("Poem2",read_file("Poem"))