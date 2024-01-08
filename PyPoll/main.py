import os
import csv

csv_file = os.path.join("Resources","election_data.csv")


total_votes = 0
candidates = {}
percentage_votes = 0



with open(csv_file) as poll_csv:
    csv_reader = csv.reader(poll_csv,delimiter=',')

    #skip header
    next(csv_reader)

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

file_location = os.path.join("analysis","election_results.txt")
with open(file_location, "w") as file:
    file.write('ELECTION RESULTS\n')
    file.write('=' * 50 + '\n')
    file.write(f'Total votes: {total_votes}\n')
    file.write('=' * 50 + '\n')
    file.write('Candidates and their votes:\n')
    
    for candidate, votes in candidates.items():
        percentage = round((votes / total_votes) * 100, 3)
        file.write(f'{candidate}: {percentage}% ({votes})\n') 
    file.write('='*50 +'\n')
    file.write(f'Election Winner: {winner}')

print(f'Results have also been sent to {file_location}')
   
   
   
   
   
    # output_file.write('ELECTION RESULTS')
    # output_file.write('='*50 + '\n')
    # output_file.write(f'Total votes: {total_votes}')
    # output_file.write('='*50)  
    # output_file.write('Candidates and their votes: ') 

    # for candidate, votes in candidates.items():
    #      percentage = round((votes/total_votes)*100,3)
    #      output_file.write(f'{candidate}:  {percentage}% ({votes})')

