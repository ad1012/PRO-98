def swapFileData():
    fileName1 = input("Enter File Name: ")
    fileName2 = input("Enter File Name: ")

    with open(fileName1, 'r') as a:
        data_a = a.read()
    
    with open(fileName2, 'r') as b:
        data_b = b.read()

    with open(fileName1, 'w') as a:
        a.write(data_b)

    with open(fileName2, 'w') as b:
        b.write(data_a)

swapFileData()