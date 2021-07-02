from read_write import read_file,write_file
from Caesar import encrypt_letter, encrypt_word, encrypt_message,decrypt_letter,decrypt_word,decrypt_message
print(encrypt_message(read_file("Poem"),1))
print(decrypt_message(encrypt_message(read_file("Poem"),1),1))
print(read_file("Poem"))
write_file("Poem2",read_file("Poem"))