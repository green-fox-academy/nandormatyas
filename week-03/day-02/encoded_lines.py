# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    fopen = open(file_name)
    fread = fopen.read()
    asci = " "
    for i in fread:
        if i != " " and i != "\n":
            i = ord(i)
            i -= 1
            i = chr(i)
            asci += i
        else:
            asci += i 

    print(asci)
file_name = 'encoded-lines.txt'
decrypt(file_name)