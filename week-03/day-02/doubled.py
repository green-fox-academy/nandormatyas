def decrypt(file_name):
    fopen = open(file_name)
    fread = fopen.read()
    decrypted = " "
    index = 0
    for i in fread[::2]:
        if i != decrypted[:index:2]:
            decrypted += i
            index += 1
    print (decrypted)

x = input('File? ')
decrypt(x)
