def read_file(location):
  file=open(location,"r")
  return file.readline().split()
def write_file(location,list_of_words):
  file=open(location,"w")
  for w in list_of_words:
    file.write(w)
write_file("Poem","This is an even longer string of gibberish.")