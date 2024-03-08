import math

inputFile = open('filename.csv', 'r')
outputFile = open('filename_new.csv', 'w')

for line in inputFile:
    result = line.replace("\n", "").split(",")
    numberOfNumbers = len(result)
    if numberOfNumbers == 0 :
        continue
    if numberOfNumbers == 1 :
        outputFile.write(result[0] + "," + result[0] + "," + "None")
        continue
    sum = 0
    for element in result:
       sum += int(element) 
       outputFile.write(element + ",")
    average = sum / numberOfNumbers
    deviation =  math.sqrt((1 / (numberOfNumbers - 1)) * ((int(result[0]) - average)**2 + (int(result[1]) - average)**2))
    outputFile.write(str(average) + "," + str(deviation) + "\n")

inputFile.close()
outputFile.close()