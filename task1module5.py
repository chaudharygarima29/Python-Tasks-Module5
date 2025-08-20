
try:
    print("Reading file content:")
    file1=open('sample.txt',"r")
    read_file=file1.readlines()
    for i in range(len(read_file)):
        print("Line", i+1,":",read_file[i])
    file1.close()
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found.")


'''
print("Reading file content:")
try:
    file1=open('sample.txt',"r")
    read_file=file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found.")
'''