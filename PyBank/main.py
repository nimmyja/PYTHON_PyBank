# This is a sample Python script.
import os
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Financial Analysis")
    csv_path = os.path.join("Resources","budget_data.csv")
    with open(csv_path,'r') as csv_file:
#Initializing the variables        
        month_count = 0
        total_amount = 0
#Change in Profit/Loss 
        total_PL_Change = 0
        prev_PL=0   
        min_PL=0
        max_PL=0
        min_month=0
        max_month=0
#Stores the rows of CSV file
        csv_reader = csv.reader(csv_file,delimiter=',')
#Stores the header from read file        
        csv_header = next(csv_reader)

        for col in csv_reader:
            month_count += 1
            total_amount += int(col[1])
#Create variable for changes in Profit/Losses
            PL_Change = int(col[1])-prev_PL
            if month_count > 1:
                if month_count == 2:
                    min_PL= PL_Change
                    max_PL= PL_Change
                    min_month= col[0]
                    max_month= col[0]
                else:
                    if (PL_Change > max_PL):
                        max_PL = int(col[1])-prev_PL
                        max_month = col[0]
                    elif (PL_Change < min_PL):
                        min_PL = PL_Change
                        min_month = col[0]
                total_PL_Change += PL_Change
            prev_PL=int(col[1])
        mean_PL = round((total_PL_Change/(month_count-1)),2)
            
#print output to terminal        
        
        print("----------------------------")
        print(f"Total Months :{month_count}")
        print(f"Total: ${total_amount}")
        print(f"Average  Change: ${mean_PL}")
        print(f"Greatest Increase in Profits: {max_month} (${max_PL})")
        print(f"Greatest Decrease in Profits: {min_month} (${min_PL})")

#write the ouput to a text file
output_path = os.path.join("Analysis","analysis.txt")
with open(output_path,'w',newline='') as datafile:
    datafile.writelines("Financial Analysis")
    datafile.writelines("\n----------------------------")
    datafile.writelines(f"\nTotal Months :{month_count}")
    datafile.writelines(f"\nTotal: ${total_amount}")
    datafile.writelines(f"\nAverage  Change: ${mean_PL}")
    datafile.writelines(f"\nGreatest Increase in Profits: {max_month} (${max_PL})")
    datafile.writelines(f"\nGreatest Decrease in Profits: {min_month} (${min_PL})")

