#importing 
import os
import csv

#setting file path
csv_file = os.path.join("Resources","election_data.csv")

#setting variables
total_votes = 0
candidates = {}
percentage_votes = 0


#opening file and using for analysis
with open(csv_file) as poll_csv:
    csv_reader = csv.reader(poll_csv,delimiter=',')
    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')
    #skip header and print headers 
    
    #looping through rows to create candidates dictionary
    for row in csv_reader:
        
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

#find winner by getting max of candidates
winner = max(candidates, key=candidates.get)
#print results

print('ELECTION RESULTS')
print('='*50)
print('total votes: ', total_votes)
print('='*50)   
print('Candidates and their votes:')
for candidate, votes in candidates.items():
    print(f'{candidate}:  {round(((votes/total_votes)*100),3)}% ({votes})')

print('='*50)
print(f'Election Winner: {winner}')
#setting file path to write to
file_location = os.path.join("analysis","election_results.txt")

#opening that file and writing in results
with open(file_location, "w") as file:
    file.write('ELECTION RESULTS\n')
    file.write('=' * 50 + '\n')
    file.write(f'Total votes: {total_votes}\n')
    file.write('=' * 50 + '\n')
    file.write('Candidates and their votes:\n')
    #looping through dictionary to count votes
    for candidate, votes in candidates.items():
        percentage = round((votes / total_votes) * 100, 3)
        file.write(f'{candidate}: {percentage}% ({votes})\n') 
    file.write('='*50 +'\n')
    file.write(f'Election Winner: {winner}')

print(f'Results have also been sent to {file_location}')
   
