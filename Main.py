import time

numOfNames = int(input('Numb of names'))
lenOfNames = int(input("Len of names"))

# Make sure lenOfNames var is more than 3 chars long.
if lenOfNames < 3:
    print('Names can\'t be less than 3 chars, silly! >:(')
    time.sleep(3)
    exit()
else:
    namesFileName = str(input("File where names will be printed"))
    if len(namesFileName.split('.')) == 2:
        pass
    elif len(namesFileName.split('.')) > 2 or namesFileName == "vars.txt" or namesFileName == "vars":
        print("invalid file name - Try something else. >:(")
        time.sleep(3)
        exit()
    else:
        namesFileName += ".txt"
    # Open file and write variables
    varFile = open("vars.txt", "w")
    varFile.writelines(['' + str(numOfNames), '\n' + str(lenOfNames), '\n' + namesFileName])
    varFile.close()

    import GenerateAndPrint  # Import statement IS used, contrary to what PyCharm thinks.
