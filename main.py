from read_write import read_file,write_file
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
from CrackingCaesar import Print_All_Messages,Crack_Cipher
from CrackingRandom import Crack_Random
from RandomSubstitution import rndms,drndms
#Crack_Cipher(read_file("CT"))
print(rndms(read_file("PT"),read_file("RSK")))
print(drndms(read_file("CT"),read_file("RSK")))