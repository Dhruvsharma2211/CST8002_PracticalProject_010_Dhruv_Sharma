#Course CST8002 - Programming Language Research Project
#Professor : Stanley Pieda
#Due Date : 1st Feb 2026
#Author : Dhruv Sharma 
# File name: dataset.py
# This file handles File input and output and loading data from CSV file
# Reference : https://realpython.com/read-write-files-python/

import csv # library usage
from record import Record # import record class

def load_dataset(file_path, max_records=2):
    records = [] #list to store record object
    try: 
        # opening CSV file 
        with open(file_path, newline='', encoding="latin1") as csv_file:
            reader = csv.DictReader(csv_file)

            # Read first few records
            for index, row in enumerate(reader):
                if index >= max_records:
                    break
                #create record object using CSV column names
                record = Record(
                    row["Site identification"],
                    row["Area"],
                    row["Visit date"],
                    row["Start time"],
                    row["Species code"],
                    row["Count"]
                )

                records.append(record)
    except FileNotFoundError:
        print(" Error :OPPPSSSSSS CSV file not found...")
    except Exception as error:
        print(f"An error occurred:{error}")
    return records