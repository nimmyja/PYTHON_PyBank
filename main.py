# This is a sample Python script.
import os
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    csv_path = os.path.join("PyBank","Resources","budget_data.csv")
    with open(csv_path,'r') as csv_file:
        total_month = 0
        total_amount = 0
        total_PL_Change = 0
        PL_Change = []
        PL_Month = []
        #month = col[0]
        prev_pl=0   
        min_pl=0
        max_pl=0
        min_month=0
        max_month=0
        csv_reader = csv.reader(csv_file,delimiter=',')
        print(csv_reader)
        csv_header = next(csv_reader)
        print(f"Header name : {csv_header}")
        for col in csv_reader:
            total_month += 1
            total_amount += int(col[1])
            if total_month > 1:
                if total_month == 2:
                    min_pl=int(col[1])-prev_pl
                    max_pl=int(col[1])-prev_pl
                    min_month= col[0]
                    max_month= col[0]
                else:
                    if ((int(col[1])-prev_pl) > max_pl):
                        max_pl = int(col[1])-prev_pl
                        max_month = col[0]
                    elif ((int(col[1])-prev_pl) < min_pl):
                        min_pl = int(col[1])-prev_pl
                        min_month = col[0]
                total_PL_Change += int(col[1])-prev_pl
            prev_pl=int(col[1])
        mean_PL = round((total_PL_Change/(total_month-1)),2)
            
        

        print(f"Total months :{total_month}")
        print(f"Total: {total_amount}")
        print(f"Average  Change: ${mean_PL}")
        print(f"Greatest Increase in Profits: {min_month} (${min_pl})")
        print(f"Greatest Decrease in Profits: {max_month} (${max_pl})")

        
