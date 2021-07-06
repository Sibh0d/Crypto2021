from read_write import read_file,write_file
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
from CrackingCaesar import Print_All_Messages,Crack_Cipher
from CrackingRandom import Crack_Random
#print(encrypt_message(read_file("Poem"),8))
#print(decrypt_message(encrypt_message(read_file("Poem"),7),7))
#print(read_file("Poem"))
#write_file("Poem2",read_file("Poem"))
#write_file("PT",decrypt_message(read_file("CT"),5))
#write_file("CT",encrypt_message(read_file("PT"),19))
#Print_All_Messages(["A","b","c"])
Crack_Cipher(read_file("PT"))
#Crack_Random(1)
Print_All_Messages(read_file("PT"))