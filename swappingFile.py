def swipeFileData():
    filename1 = input("Enter the name of the first file: ")
    filename2 = input("Enter the name of the second file: ")
    with open(filename1, 'r') as a:
        data_a = a.read()
    with open(filename2, 'r') as b:
        data_b = b.read()
    with open(filename1, 'w') as a:
        a.write(data_b)
    with open(filename2, 'w') as b:
        b.write(data_a)
    print("File data has been switched!")

swipeFileData()