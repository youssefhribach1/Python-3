


# the file management

#open(filename,access,buffering)

file=open("C:\\Users\\YOUSSEF HRI\\Desktop\\test.txt","r")
print(file.read())
file.close()

# print(file.read(10))
 # print(file.tell())
 # file.seek(5)

#writting file

file=open("write.txt","w+")
file.write("hello file . i am string!")
file.seek(0)

