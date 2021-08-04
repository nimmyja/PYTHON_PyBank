# This is a sample Python script.
import os
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_line():
    print("-------------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Election results')
    print_line()
    csv_path = os.path.join("Resources","election_data.csv")
    total_votes = 0
    with open(csv_path,'r') as csv_file:
        csv_reader =  csv.reader(csv_file,delimiter=',')
        
        csv_header = next(csv_reader)   #Skip the header row
        cand_arr = []   # Store candidates name in a list
        
        for row in csv_reader:
            total_votes +=1
            cand_name = row[2]
            cand_arr.append(row[2])  

        unique_items = list(dict.fromkeys(cand_arr))    

        print(f"Total Votes : {total_votes}")
        print_line()
        winner = 0
        for candidate in unique_items:
            cand_votes = cand_arr.count(candidate)            
            cand_percent ="{:.3%}".format(cand_votes/total_votes)

            print(f"{candidate} : {cand_percent} ({str(cand_votes)})")
            
            if winner < cand_votes:
                winner = cand_votes
                cand_won = candidate
        print_line()                      
        print(f"Winner : {cand_won}")
        print_line()
        
                
                

            
        

        

            

