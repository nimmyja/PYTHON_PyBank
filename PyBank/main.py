import os
import csv

#module to print the name of the analysis
def print_hi(name):
    print(f'{name}')

#module to print the name of the analysis
def print_line():
    print("----------------------------")


if __name__ == '__main__':
    print_hi("Financial Analysis")
    csv_path = os.path.join("Resources","budget_data.csv")
    with open(csv_path,'r') as csv_file:

        #Initialize required variables        
        month_count = 0
        total_amount = 0
        total_PL_Change = 0
        prev_PL=0   
        min_PL=0
        max_PL=0
        min_month=0
        max_month=0

        #Stores the rows of CSV file
        csv_reader = csv.reader(csv_file,delimiter=',')
        #Skip the header row        
        csv_header = next(csv_reader)

        for col in csv_reader:
            month_count += 1
            total_amount += int(col[1])
        #Variable to store changes in Profit/Losses
            PL_Change = int(col[1])-prev_PL
        #Calculating the changes in Profit/Losses    
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
        print_line()
        print(f"Total Months :{month_count}")
        print(f"Total: ${total_amount}")
        print(f"Average  Change: ${mean_PL}")
        print(f"Greatest Increase in Profits: {max_month} (${max_PL})")
        print(f"Greatest Decrease in Profits: {min_month} (${min_PL})")

#write the ouput to a text file
output_path = os.path.join("Analysis","output.txt")
with open(output_path,'w',newline='') as datafile:
    datafile.writelines("Financial Analysis")
    datafile.writelines("\n----------------------------")
    datafile.writelines(f"\nTotal Months :{month_count}")
    datafile.writelines(f"\nTotal: ${total_amount}")
    datafile.writelines(f"\nAverage  Change: ${mean_PL}")
    datafile.writelines(f"\nGreatest Increase in Profits: {max_month} (${max_PL})")
    datafile.writelines(f"\nGreatest Decrease in Profits: {min_month} (${min_PL})")

