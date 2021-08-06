# Import Modules
import os
import csv

def print_hi(name):
    print(f'{name}')  


def print_line():
    print("-------------------------")


if __name__ == '__main__':
    print_hi('Election results')
    print_line()
    csv_path = os.path.join("Resources","election_data.csv")
    total_votes = 0
    with open(csv_path,'r') as csv_file:
        csv_reader =  csv.reader(csv_file,delimiter=',')
        #Skip the header row
        csv_header = next(csv_reader)   
        # Store candidates name in a list
        cand_arr = []   
        
        for row in csv_reader:
            total_votes +=1
            cand_name = row[2]
            cand_arr.append(row[2]) 

        #Identify unique candidate names from the candidate list
        unique_items = list(dict.fromkeys(cand_arr))    

        #Printing Total number of votes
        print(f"Total Votes : {total_votes}")
        print_line()
        winner = 0
        for candidate in unique_items:
            cand_votes = cand_arr.count(candidate)            
            cand_percent ="{:.3%}".format(cand_votes/total_votes)

            #Printing Total number and percentage of votes each candidate won
            print(f"{candidate} : {cand_percent} ({str(cand_votes)})")
            
            #Finding winner of the election
            if winner < cand_votes:
                winner = cand_votes
                cand_won = candidate
        print_line()                      
        print(f"Winner : {cand_won}")
        print_line()

#Writing ouput to text file
output_path = os.path.join("Analysis","output.txt")
with open(output_path,'w',newline='') as writer:
    writer.writelines("Election results")
    writer.writelines("\n----------------------------")
    writer.writelines(f"\nTotal Votes : {total_votes}")
    writer.writelines("\n----------------------------")
    for candidate in unique_items:
        cand_votes = cand_arr.count(candidate)            
        cand_percent ="{:.3%}".format(cand_votes/total_votes)
        writer.writelines(f"\n{candidate} : {cand_percent} ({str(cand_votes)})")
    writer.writelines("\n----------------------------")                      
    writer.writelines(f"\nWinner : {cand_won}")
    writer.writelines("\n----------------------------")
    




        
                
                

            
        

        

            

