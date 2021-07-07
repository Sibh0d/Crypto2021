from read_write import read_file,write_file
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
from CrackingCaesar import Print_All_Messages,Crack_Cipher
from CrackingRandom import Crack_Random
from RandomSubstitution import rndms,drndms
from CrackingRandom import Crack_Random
#Crack_Cipher(read_file("CT"))
#print(rndms(read_file("PT"),read_file("RSK")))
#print(drndms(read_file("CT"),read_file("RSK")))
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersd={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
words=read_file("Textforfrequency")
ln=0
for w in words:
  for l in w:
    if l.lower() in letters:
      ln+=1
      lettersd[l.lower()]+=1
for x in lettersd:
  lettersd[x]=100*lettersd[x]/ln
  print(x, end=" ")
  print(lettersd[x])
print("\n"*4)
Crack_Random(read_file("CT"))