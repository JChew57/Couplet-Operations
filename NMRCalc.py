def finalResult(list, numCouplets):
    #Adds all final data together and divides it by the number of couplets
    #Multiplied by 500 for the machine used at SFSU
    i = 0
    num = 0
    length = len(list)
    while i < (length-1):
        num += list[i]
        i += 1
    num = (num/numCouplets)*500
    return (num)

def coupletsStep1(coupletList):
    #Subtracts data in couplet pairs and and appends results to a list to have
    #final procedures done on them in finalResult
    i = 0
    resultList = []
    length = len(coupletList)
    modlength = length % 2
    inBounds = True
    counter = 1 #keeps track of number of couplets
    print("----------Subtraction Results for each couplet----------")
    #Specific Check for data lists that are odd numbered in length.
    if modlength == 1:
        while inBounds:
            farI = i + 2
            if i > 0:
                if i == (length/2 - 0.5):
                    i+=1
                    farI = i + 2
                if farI >= length:
                    inBounds = False
                else:
                    result = coupletList[i+1] - coupletList[farI]
                    print(result)
                    resultList.append(result)
                    i += 1
                    counter+=1
            else:
                result = coupletList[i] - coupletList[i+1]
                print(result)
                resultList.append(result)
                i +=1
    else:
        while inBounds:
            farI = i + 2
            if i > 0:
                if farI >= length:
                    inBounds = False
                else:
                    result = coupletList[i+1] - coupletList[i+2]
                    print(result)
                    resultList.append(result)
                    i += 1
                    counter = i
            else:
                result = coupletList[i] - coupletList[i+1]
                print(result)
                resultList.append(result)
                i +=1
    final = finalResult(resultList, counter)
    print("--------------------------------------------------------")
    print ("Final Result: " + str(final) + "\n")

def coupletsStep2(coupletList):
    #Same as coupletsStep1 but now operations done on every other value
    i = 0
    resultList = []
    inBounds = True
    print("----------Subtraction Results For Second Step Couplets----------")
    while inBounds:
        farI = i+2
        if farI >= len(coupletList):
            inBounds = False
        else:
            result = coupletList[i] - coupletList[i+2]
            print (result)
            resultList.append(result)
            i += 1
    final = finalResult(resultList, i)
    print("----------------------------------------------------------------")
    print("Final Result: " + str(final) + "\n")

repeat = True
while repeat:
    #Create/Open file and write user input into the file
    filename = "data.txt"
    data = input("Enter your data. Seperate using space (Type q to quit): ")
    list = []
    with open(filename, 'w') as file_object:
         file_object.write(data)

    with open(filename) as file_object:
         for line in file_object:
             for item in line.split():
                 list.append(item)

    #Convert strList to a list of floats
    if list[0] == 'q':
        print("Program Ended\n")
        repeat = False
    else:
        dataList = []
        for num in list:
            floatNum = float(num)
            dataList.append(floatNum)
        coupletsStep1(dataList)
        coupletsStep2(dataList)
        print("Done!\n")
