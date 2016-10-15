def finalResult(list, numCouplets):
    #Adds all final data together and divides it by the number of couplets
    i = 0
    num = 0
    length = len(list)
    while i < (length-1):
        num += list[i]
        i += 1
    num = num/numCouplets
    return (num)

def coupletsStep1(coupletList, numCouplets):
    #Subtracts data in couplet pairs and and appends results to a list to have
    #final procedures done on them in finalResult 
    i = 0
    resultList = []
    print("----------Subtraction Results for each couplet----------")
    while i < numCouplets:
        if i > 0:
            result = coupletList[i+2] - coupletList[i+1]
            print(result)
            resultList.append(result)
            i += 1
        else:
            result = coupletList[i+1] - coupletList[i]
            print(result)
            resultList.append(result)
            i +=1
    final = finalResult(resultList, numCouplets)
    print("--------------------------------------------------------")
    print ("Final Result: " + str(final) + "\n")

def coupletsStep2(coupletList, numCouplets):
    #Same as coupletsStep1 but now operations done on every other value
    i = 0
    resultList = []
    print("----------Subtraction Results For Second Step Couplets----------")
    while i < numCouplets:
        result = coupletList[i+2] - coupletList[i]
        print (result)
        resultList.append(result)
        i += 1
    final = finalResult(resultList, numCouplets)
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
        numCouplets = len(dataList)/2
        coupletsStep1(dataList, numCouplets)
        coupletsStep2(dataList, numCouplets)
        print("Done!\n")
