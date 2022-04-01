my_company=open("files.txt","r")
for work in my_company.readlines():
    print(work)
my_company.close()
#r stands for read we use it just to access files to see what is in the files
#w stands for write we access ,modify or add another things in files
#r+ stands for read and write we use it to read and write 
#a stands for append we use append to access a file ut we are not allowed to change content what we are allowed to do is to add another contents
