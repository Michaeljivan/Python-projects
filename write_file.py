
#write file name
filename = "newfile1.txt"

myfile = open(filename, 'a')

myfile.write('Hello World again\n')
myfile.close()