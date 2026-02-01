#Course CST8002 - Programming Language Research Project
#Professor : Stanley Pieda
#Due Date : 1st Feb 2026
#Author : Dhruv Sharma 
# File name: dataset.py
# This file program entry 
#Reference : L. P. Ramos, "method," 19 Sep 2025. [Online]. Available: https://realpython.com/ref/glossary/method/. [Accessed 01 Feb 2026].
from dataset import load_dataset

# Constants
FULL_NAME = "DHRUV SHARMA"
CSV_FILE = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

def main():
    print("=" * 100)
    print(f"Student Name: {FULL_NAME}")
    print("=" * 100)

    # Load dataset 
    
    records = load_dataset(CSV_FILE)

    # Loop through records and display from
    if records:
        print("\nDataset Records: \n")
        for record in records:
            print(record)
    else:
        print("No records loaded....")
    
    print("\n" + "=" * 80)
    print(f"Student Name: {FULL_NAME}")
    print("="* 80)

    #start program 
if __name__ == "__main__":
        main()