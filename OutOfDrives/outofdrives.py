#!/usr/bin/env
import csv

# read the CSV file and find the Offline-Drivers
def find_drives(): 
    count = 0
    try:
        with open('input.txt', 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if row[1].strip() == 'Offline':
                    count += 1

                    get_drive_name(row)

                    for i in range(2, len(row)):
                       adapted_row = row[i].strip()
                       adapted_row = adapted_row.split(' ', 1)
                       print('\t ' + '{key}: {value}'.format(key=adapted_row[0], value=adapted_row[1]))

                    print("\n")

    except FileNotFoundError:
        print("ERROR! Couldn't open file to read:\nplease make sure correct file ('input.txt') is on same base folder")

    return count

# manipulating drive's name:
def get_drive_name(row):
    drive_name = row[0].split(':', 1)[-1]
    drive_name = drive_name.strip()
    drive_name = drive_name.split(' ', 1)
    print('{key}: {value}'.format(key=drive_name[0], value=drive_name[1]))

if __name__ == "__main__":
    OFFLINE_DEVICES = find_drives()
    print("There are [{}] Offline Drives".format(OFFLINE_DEVICES))
