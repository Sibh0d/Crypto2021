from read_write import read_file,write_file,print_message
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
from CrackingCaesar import Print_All_Messages,Crack_Caesar
from RandomSubstitution import rndms,drndms,generate_key
from CrackingRandom import Crack_Random
from Vigenere import VigenereM,DVigenereM
from CrackingVigenere import getIOC, getKeyLen
from Affine import AEM,ADM
#write_file("CT",VigenereM(read_file("PT"),'Goodbye')) #Closer though not working yet
#print(getKeyLen(read_file("CT")))
#print(print_message(ADM(AEM(read_file("PT"),[15,29]),[15,29])))
from CrackingAffine import CrackAffine
