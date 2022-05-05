# Import python modules.
from alive_progress import alive_bar
from datetime import datetime, timedelta
from os.path import exists
import os
import csv

# Year to check
year = 2022
# Number of months to check in the year. 3 = Jan to March
months = 12

# Folder that the .csv files are in.
folder = "files"


finaloutput = []

finaloutput.append("============================================== AWE REPORT ==========================================================")
# print("============================================== AWE REPORT ==========================================================")
# Function to make sure the cell we are using provides a vaild date, if not skip the cell. 
# (Due to comma issues with game names which shifts the cells over and breaks the code.)



def is_valid_date(user_date):
    try:
        datetime.strptime(user_date, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        return False
    return True


# Main Code Loop
for filename in os.listdir(folder):  # For each csv file in the folder.
    with alive_bar(title_length=30, title=f'Processing {filename}', bar='solid', length=3, spinner='waves2', spinner_length=10) as bar:
        month = 1  # Month counter for the while loop.
        f = os.path.join(folder, filename)  # Get the full file path.
        finaloutput.append(" ")
        finaloutput.append(f"---------------{f}---------------")

        # print("")
        # print(f"---------------{f}---------------")
        while month <= (months): # Only check for subset of months. Example <=3 = Jan - March
            if exists(f):
                print(f"file = {f}")
                with open(f, "r") as info:
                    data = list(csv.reader(info)) # Get all rows as lists.
                    count = 0 # Keep track of month number for report printout
                    total_time = datetime.min  # Create a blank datetime object to hold total session time.
                    for i in data[7:]:  # Skip the first 6 rows. They conatin no session data.
                        # Strip any leading or trailing spaces.
                        i[0] = i[0].strip()
                        i[1] = i[1].strip()
                        i[2] = i[2].strip()
                    
                        if all([is_valid_date(i[1]), is_valid_date(i[2])]):  # Run function above to check for valid date in the two cells.
                            # Convert date and time cells to python datetime objects
                            dt1 = datetime.strptime(i[1], "%m/%d/%Y %I:%M:%S %p")
                            dt2 = datetime.strptime(i[2], "%m/%d/%Y %I:%M:%S %p")

                            if i[0] == "Session":
                                if dt1.month == month and dt1.year == year:  # Only count the month and years we want.
                                    count += 1  # Go to next month number for report
                                    print(f"dt2 = {dt2} ~ dt1 = {dt1}")
                                    total_time += (dt2 - dt1)  # Add up session time from datetime objects

                    totalseconds = (total_time.hour * 60 + total_time.minute) * 60 + total_time.second
                    try:
                        sessionseconds = totalseconds / count

                        finaloutput.append(" ")
                        finaloutput.append(f"Total Sessions for {month}/{year}:   {count}")
                        finaloutput.append(f"Total Time For Month {month}/{year}: {str(total_time.hour) + ':' + str(total_time.minute) + ':' + str(total_time.second)}")

                        # print("")        
                        # print(f"Total Sessions for {month}/{year}:   {count}")  
                        # print(f"Total Time For Month {month}/{year}: {str(total_time.hour) + ':' + str(total_time.minute) + ':' + str(total_time.second)}")
                        ##### print(f"Total Time For Month {month}/{year}: {total_time.hour} HOURS  {total_time.minute} MINUTES")
                        dtaverage = timedelta(seconds = sessionseconds)
                        finaloutput.append(f"Average Session Time: {''.join(str(dtaverage).split('.')[0])}")
                        # print(f"Average Session Time: {''.join(str(dtaverage).split('.')[0])}")



                    except ZeroDivisionError:
                        finaloutput.append(" ")
                        finaloutput.append(f"Zero results in: {filename}, for month: {month}")

                        # print(" ")
                        # print(f"Zero results in: {filename}, for month: {month}")
                        
                        pass
                        

            bar()
            month += 1  # Go to next month until we hit our max requested


with open('stats.txt', 'w') as output_file:
    for i in finaloutput:
        output_file.write(i + '\n')

for i in finaloutput:
    print(i)
    
