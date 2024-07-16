#Open the CSV file using the provided file location and return instance of reader 
def readCSVFile(cvsFilePath):
    #Open the CSV file providing the path and encoding info
    with open(cvsFilePath, encoding='UTF-8') as csvfile:
        #Get the reader instance to read the contents from the file
        csvReader = csv.reader(csvfile, delimiter=',')
        return list(csvReader)

#Method will count the occurrence of the data in the data_rows to provide a 
# dictonary with the value as the key and its occurence count as value         
def columnDataCount(data_rows):
    count = 0
    #Loop through the reader to read the data in the file
    for row in data_rows:
        #Running counter for number of entries 
        count = count + 1
        candidate = row[2]   
        candidateVoteCount = output_dict.get(candidate,0)
        #Count the vote for the candidates
        if candidateVoteCount > 0:
            candidateVoteCount = candidateVoteCount + 1
        else:
            candidateVoteCount = 1
        output_dict[candidate] = candidateVoteCount
    return output_dict

#Method to write the text to the file
def writetoFile(outputFilePath, textToWrite):    
    # Open the file in write mode and write the DataFrame string
    with open(outputFilePath, 'w') as file:
        file.write(textToWrite)

#Print vote-counting information
import os
import csv
from pathlib import Path

seperator = "-" * 25
analysisStr = ["Election Results",seperator] 
#Read data from the CSV file
csvReader = readCSVFile("Resources/election_data.csv")
csvHeader = csvReader[0] #Skip the header row
data_rows = csvReader[1:]
#Store the calculated candidate name and its vote count
output_dict = {}

highestVoteCount = 0

output_dict =  columnDataCount(data_rows)
totalVoteCount = sum(output_dict.values())
#Append the total vote count Msg
totalVoteMsg = f"Total Votes: {totalVoteCount}"
analysisStr.append(totalVoteMsg)
analysisStr.append(seperator)
for key,value in output_dict.items():
    if value > highestVoteCount:
        highestVoteCount = value
        winner = key
    percentOfTotalVote = round((value/totalVoteCount)*100,3)
    percentCalStr = f"{key}: {percentOfTotalVote}% {value}"
    #Append the percentage of vount count
    analysisStr.append(percentCalStr)
analysisStr.append(seperator)
#Append the winner name
winnerStr = f"Winner {winner}"
analysisStr.append(winnerStr)
analysisStr.append(seperator)
# Convert all items to strings
analysisStr = [str(item) for item in analysisStr]
mergedStrMsg = "\n".join(analysisStr)
#print on the terminal
print(mergedStrMsg)
#write on the output file
writetoFile("analysis/PollAnalysis.txt", mergedStrMsg)

