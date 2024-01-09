import os
import csv


csv_file = os.path.join("Resources","budget_data.csv")

#assign variables

total_months = 0
net_total = 0
previous_gain_loss = 0

#assign variable lists to store for sorting later
change_in_money = []
months =[]

#open and read the csv file
with open(csv_file) as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter=',')
    csv_header = next(csv_reader)
    print(f'CSV_header: {csv_header}')
    #skip header row
    
    
    #looping through rows and gathering data
    for row in csv_reader:
            #print(row)
            
            
            #add one to the month count for each row
            total_months += 1
            
            #store gain/loss for month as gain_loss
            gain_loss = int(row[1])
            
            #running total of change is just adding each row's gain_loss together
            net_total += gain_loss
            
            #if we are past the first row follow this
            if total_months > 1:
                
                #calculating each rows change as the gain_loss of 2nd column minus the previous columns value and storing
                change = gain_loss - previous_gain_loss
                #storing previous value in a list called change_in_money
                change_in_money.append(change)
                #adding date to a list called months to reference later
                months.append(row[0])
            #store first row's gain loss as previous    
            previous_gain_loss = gain_loss
    #calculations for statiistical analysis   
    average_change = sum(change_in_money)  / len(change_in_money)
    
    
    average_change_rounded = round(average_change,2)   #rounding to two decimal places to put in dollar format
    greatest_increase = max(change_in_money)  
    greatest_loss = min(change_in_money)
    
    increase_index = change_in_money.index(greatest_increase) 
    decrease_index = change_in_money.index(greatest_loss)
    date_greatest = months[increase_index]
    date_smallest = months[decrease_index]

    print('Financial Analysis:')
    print('='*100)
    print(f'Total Months: {total_months}')
    print(f'Total:  ${net_total}')
    print(f'Average change is (${average_change_rounded})')
    print(f'Greatest increase in profits:  {date_greatest} (${greatest_increase})')
    print(f'Greatest decrease is {date_smallest} (${greatest_loss})')
    
    #creating variables for list to print to file
    line_1 = ('Financial Analysis:')
    line_2 = ('='*100)
    line_3 = (f'Total Months: {total_months}')
    line_4 = (f'Total:  ${net_total}')
    line_5 = (f'Average change is (${average_change_rounded})')
    line_6 = (f'Greatest increase in profits:  {date_greatest} (${greatest_increase})')
    line_7 = (f'Greatest decrease is {date_smallest} (${greatest_loss})')
    
    #creating list
    lines = [line_1,line_2,line_3,line_4,line_5,line_6,line_7]
   
    #setting path for writing txt file
    file_name = ("analysis.txt")
    output_folder = ("analysis")
    output_name = os.path.join(output_folder,file_name)
    #opening that file and writing in info
    with open(output_name, 'w') as file:
    
        #adding '\n' for line break
        for line in lines:
            file.write(line + '\n')
        
       

