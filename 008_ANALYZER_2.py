""" whenever I say "this is the code that", it means im referring to the code written below"""

from datetime import datetime
import csv
import os
import shutil

''' this below portion of the code is used to extract date and time which will be used to identify
when the alert files were created ( we will add it to the folder name ) '''

curr_date_and_time = datetime.now()
curr_date = curr_date_and_time.date()
curr_time = curr_date_and_time.strftime('%H:%M:%S')
curr_date = str(curr_date)
curr_time = str(curr_time)
curr_time = curr_time.replace(":", "-")  # because colon becomes a problem when naming a csv file

''' now ofcourse if there are no info files to check then the program should terminate '''

csv_files = [filename for filename in os.listdir() if filename.endswith('.csv')]
if len(csv_files) == 1:
    print("there are no info files to check.. terminating program")
    exit()

client_fol_name = ''  # we will store the name of the client's computer in this variable and name
# the folder this name

# extract all files that start with 'PROINFO' because those contain information about processes
proinfo_files = [filename for filename in os.listdir() if filename.startswith('PROINFO')]

pro_file = proinfo_files[0]  # extract the first of those files (actually we only have one so..)

''' this is the csv file handling part where we read the PROINFO file, then we read the process_blacklist 
file, and whatever matches we entry that data into a new file, namely 'PROALERT'  '''

with open("PROALERT.csv", 'w') as nfile:
    writer = csv.writer(nfile)
    data1 = ["line number (in PROINFO.csv)", "processname", "processid", "danger level"]
    writer.writerow(data1)
    with open(pro_file, 'r') as file1:
        reader1 = csv.reader(file1)
        with open('PROCESS_BLACKLIST.csv', 'r') as file2:
            reader2 = csv.reader(file2)
            i = 0
            for row1 in reader1:
                file2.seek(0)
                if i == 0:
                    client_fol_name = row1[1]  # the first line contains the name of the client's computer
                elif i == 1:
                    pass
                else:
                    for row2 in reader2:
                        if row1[1] == row2[0]:
                            data2 = [i + 1, row1[1], row1[0], row2[1]]
                            writer.writerow(data2)
                i = i + 1

''' now to do the same thing for net info'''

netinfo_files = [filename for filename in os.listdir() if filename.startswith('NETINFO')]

net_file = netinfo_files[0]  # extract the first of those files (actually we only have one so..)

with open("IPALERT.csv", 'w') as nfile:
    writer = csv.writer(nfile)
    data1 = ["line number (in NETINFO.csv) ", "processid", "remote ip", "remote port number", "danger level"]
    writer.writerow(data1)
    with open(net_file, 'r') as file1:
        reader1 = csv.reader(file1)
        with open('IP_BLACKLIST.csv', 'r') as file2:
            reader2 = csv.reader(file2)
            i = 0
            for row1 in reader1:
                file2.seek(0)
                if i <= 1:
                    pass
                else:
                    for row2 in reader2:
                        if row1[4] == row2[0]:
                            data2 = [i + 1, row1[0], row1[4], row1[5], row2[1]]
                            writer.writerow(data2)
                i = i + 1

''' this is the portion of the code which creates a new folder to shift all the related files to'''

# adding the date and time to folder name as we promised above
client_fol_name += " " + curr_date
client_fol_name += " " + curr_time

# we don't want to move the blacklist file to the folder. this comes in handy.
file_to_keep1 = 'PROCESS_BLACKLIST.csv'
file_to_keep2 = 'IP_BLACKLIST.csv'

os.makedirs(client_fol_name)

csv_files.append("PROALERT.csv")  # because earlier we didn't have the PROALERT file, now we do so we should
# consider that as well
csv_files.append("IPALERT.csv")  # this too

for file in csv_files:
    if file != file_to_keep1 and file != file_to_keep2:
        shutil.move(file, os.path.join(client_fol_name, file))

print("moved essential filed to folder ", client_fol_name)
