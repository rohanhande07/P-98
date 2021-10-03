def swapFileData():
    file1Name = input("Enter the first file name: ")
    file2Name = input("Enter the second file name: ")
    with open(file1Name, 'r') as a:
        dataA = a.read()
    with open(file2Name, 'r') as b:
        dataB = b.read()
    with open(file1Name, 'w') as a:
        a.write(dataB)
    with open(file2Name, 'w') as b:
        b.write(dataA)

swapFileData()