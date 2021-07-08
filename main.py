from read_write import read_file,write_file,print_message
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
from CrackingCaesar import Print_All_Messages,Crack_Cipher
from RandomSubstitution import rndms,drndms,generate_key
from CrackingRandom import Crack_Random
from Vigenere import VigenereM,DVigenereM
print(print_message(Crack_Random(read_file("CT"))[0]))
print(Crack_Random(read_file("CT"))[1])
#print(read_file("CT"))
#print(drndms(read_file("CT"),['m', 'w', 'n', 'q', 'b', 'x', 'v', 'i', 'l', 'y', 'a', 's', 'c', 'k', 't', 'j', 'p', 'z', 'u', 'r', 'o', 'f', 'd', 'h', 'g', 'e']))
#print(DVigenereM(VigenereM(read_file("Words"),"hello"),"hello"))
#write_file("CT",rndms(read_file("PT"),generate_key()))
"""text=[]
for x in read_file("Textforfrequency"):
  text.append(x.strip())
write_file("Textforfrequency",text)"""