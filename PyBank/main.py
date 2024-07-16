#Method to calculate the change in the dataset provided as input parameter
def calculateChangeInData(data_dict):
    changeInAmt_dict = {}
    keys = list(data_dict.keys())
    for i in range(len(keys) - 1):
        current_key = keys[i]
        next_key = keys[i + 1]
        #Calculate the changes in Profit/Losses data
        changeInAmt = data_dict[next_key] - data_dict[current_key]
        #Store the change in amount along with the Date Info
        changeInAmt_dict[next_key] = changeInAmt
    #Sort the dictionary with change in amount in descending order
    sorted_dict_desc = {key: value for key, value in sorted(changeInAmt_dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict_desc 

#Open the CSV file using the provided file location and return instance of reader 
def readCSVFile(cvsFilePath):
    #Open the CSV file providing the path and encoding info
    with open(cvsFilePath, encoding='UTF-8') as csvfile:
        #Get the reader instance to read the contents from the file
        csvReader = csv.reader(csvfile, delimiter=',')
        return list(csvReader)

#Method to write the text to the file
def writetoFile(outputFilePath, textToWrite):    
    # Open the file in write mode and write the DataFrame string
    with open(outputFilePath, 'w') as file:
        file.write(textToWrite)

import os
import csv
from pathlib import Path

output_dict = {}
profitLossColumnData = {}
#Create the Path for the CSV File
cvsFilePath = os.path.join("Resources","budget_data.csv")
csvReader = readCSVFile(cvsFilePath)
csvHeader = csvReader[0] #Skip the header row
data_rows = csvReader[1:]

    #Loop through the reader to read the data in the file
for row in data_rows:
    #Read the Date Info
    dateInfo = row[0]     
    #Read the profit/loss amount
    profitLossAmt = int(row[1])
    profitLossColumnData[dateInfo] = profitLossAmt

seperator = "-" * 25      
totalMonthsStr = f"Total Months: {len(profitLossColumnData)}"
totalAmtStr = f"Total : ${sum(profitLossColumnData.values())}"
#The changes in "Profit/Losses" over the entire period
output_dict = calculateChangeInData(profitLossColumnData)
averageChange = round(sum(output_dict.values())/len(output_dict),2)
averageChngStr = f"Average Change : ${averageChange}"
#Get the greatest increase in profits along with its Date info
first_key, first_value = list(output_dict.items())[0]
greatestIncStr = f"Greatest Increase in Profits: {first_key} ${first_value}"
#Get the greatest decrease in profits along with its Date info
last_key, last_value = list(output_dict.items())[len(output_dict)-1]
greatestDecStr =f"Greatest Decrease in Profits: {last_key} ${last_value}"

analysisStr = ["Financial Analysis",seperator,totalMonthsStr,totalAmtStr,averageChngStr,greatestIncStr,greatestDecStr]
# Convert all items to strings
analysisStr = [str(item) for item in analysisStr]
mergedStrMsg = "\n".join(analysisStr)
#print on the terminal
print(mergedStrMsg)
#write on the output file
writetoFile("analysis/BankAnalysis.txt", mergedStrMsg)
