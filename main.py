from read_write import read_file,write_file
print(read_file("Poem"))
write_file("Poem2",read_file("Poem"))