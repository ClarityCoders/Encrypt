def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    


choice = ""
while choice != "3":
    print("Please select you option.")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("Enter a key as int!\n"))
        filename = input("Enter filename with extension:\n")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)