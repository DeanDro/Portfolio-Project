
# Microservice by Nicolas Fong to sort the content of a list

import time

isrunning = True

while (isrunning == True):
    commandfile = open("./Microservice_Nicolas_Fong/commands.txt","r")
    #print("waiting")
    #time.sleep(5)

    if (commandfile.read() == 'sort'):
        commandfile.close()
        #print("sorting")
        #isrunning = False

        datafile = open("./Microservice_Nicolas_Fong/data.txt","r+")
        filearray = datafile.readlines()
        filearray.sort()
        #print(filearray)
        datafile.close()

        datafile = open("./Microservice_Nicolas_Fong/data.txt","w+")
        
        for i in range(len(filearray)):
            #print(i)
            datafile.write(filearray[i])

        datafile.close()
        commandfile = open("./Microservice_Nicolas_Fong/commands.txt","w")
        commandfile.write('done')
    time.sleep(5)
