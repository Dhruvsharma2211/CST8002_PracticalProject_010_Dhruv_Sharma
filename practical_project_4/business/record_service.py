"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
Business Layer : in-memory list + CRUD
File name : record_service.py
This file contains the business logic of the application including CRUD operation and sorting algorithm implemented for the project 3.
The RecordService class provides methods to manage records in memory, including loading data from a CSV file, adding, updating, deleting records, and sorting them based on specified fields. It also includes methods to parse sort and search expressions from text input. The service interacts with the CsvRepository to load and export data as needed.
Reference:


[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
[7] 	Parks Canada, "Migratory Shorebird Habitat Use - Pacific Rim," open.canada.ca, 01 Oct 2017. [Online]. Available: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697. [Accessed 02 April 2026].
[8] 	www.geeksforgeeks.org, "Searching Algorithms in Python," www.geeksforgeeks.org, 04 Sep 2025. [Online]. Available: https://www.geeksforgeeks.org/dsa/searching-algorithms-in-python/. [Accessed 10 April 2026].
[9] 	R. Sharma, "Master Searching algorithms With Python in one shot," Medium.com, 21 June 2024. [Online]. Available: https://medium.com/pythoneers/master-searching-algorithms-with-python-in-one-shot-5f9eec198d43. [Accessed 12 04 2026].


"""


from typing import List, Optional, Dict
from practical_project_4.model.record import Record, FIELDS
from practical_project_4.persistence.csv_repository import CsvRepository
from typing import Tuple 
SortInstruction = Tuple[str, bool] 
SearchInstruction = Tuple[str, str]
"""This file contains the business logic of the application including CRUD operation and sorting algorithm implemented for the project 3.       
The RecordService class provides methods to manage records in memory, including loading data from a CSV file, adding, updating, deleting records, and sorting them based on specified fields. It also includes methods to parse sort and search expressions from text input. The service interacts with the CsvRepository to load and export data as needed.
"""
class RecordService:
    def __init__(self, repo: CsvRepository) -> None:
        """Initialize the RecordService with a CSV repository.
        Args:      repo (CsvRepository): The repository to load and save records.
        Returns:    None    
        """
        self.repo = repo
        self.records: List[Record] = []

    def startup_load(self) -> None:
        """Load the first 100 records from the CSV file into memory when the application starts.
        Returns:      None  
        """
        self.records = self.repo.load_first_100()
    
    def reload(self) -> None:
        """Reload the dataset, replacing the in-memory data with the first 100 records from the CSV file.       
        Returns:      None
        """
        self.records = self.repo.load_first_100()

    def export(self) -> str:
        """Export the current in-memory records to a new CSV file with a UUID filename.
        Returns:      str: The file path of the exported CSV file.
        """
        return str(self.repo.export_to_new_csv(self.records))
    
    def list_all(self) -> List[Record]:
        """List all records currently in memory.
        Returns:      List[Record]: A list of all records currently stored in memory.           
        """
        return self.records


    def get_by_index(self, index: int) -> Optional[Record]:
        """Get a record by its index in the list.
        Args:         index (int): The index of the record to retrieve.
        Returns:      Optional[Record]: The record at the specified index, or None if the index is out of range.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None
    def add(self, record: Record) -> None:
        """Add a new record to the in-memory list.
        Args:         record (Record): The record to add.       
        Returns:      None
        """
        self.records.append(record)
    
    def update(self, index: int, record: Record) -> bool:
        """Update a record at a specific index.
        Args:         index (int): The index of the record to update.
               record (Record): The new record data to replace the existing record.
        Returns:      bool: True if the update is successful, otherwise False.      
        """
        if 0 <= index < len(self.records):
            self.records[index] = record
            return True
        return False
    
    def delete(self, index: int) -> bool:
        """Delete a record by index.
        Args:         index (int): The index of the record to delete.       
        Returns:      bool: True if deletion is successful, otherwise False.
        """
        if 0 <= index < len(self.records):
            self.records.pop(index)
            return True
        return False
    
    def search_by_selected_fields(self, criteria: dict):
        return self.service.search_by_selected_fields(criteria)
    
    def sort_records(self, field_name: str, descending: bool = False) -> bool:
        """
        Sort records based on a selected dataset column.
        THis method implements the project 3 requirement
        
        Args:
            Fileld_name  (str): Filed used for sorting
            descending(bool): True for descending order.
        
        returns: 
        bool: True IF soting successful, otherwise False.
        """ 
        
        if field_name not in FIELDS:
            return False
        def sort_key(record: Record):
            value = str(record.get_value(field_name)).strip()
            if field_name == "Count":
                try:
                    return int(value)
                except ValueError:
                    return 0
            return value.lower()
        self.records = sorted(self.records, key=sort_key, reverse=descending)
        return True
    def sort_records_multi(self, instructions): #Dhruv Sharma
        """Sort records based on multiple sort instructions.
        Args:
            instructions (List[SortInstruction]): A list of sort instructions as (field, descending) tuples.
        Returns:
            bool: True if sorting is successful, otherwise False.
        """
        if not instructions:
            return False
        for field_name, _ in instructions:
            if field_name not in FIELDS:
                return False
        for field_name, descending in reversed(instructions):
            if field_name not in FIELDS:
                return False
        for field_name, descending in reversed(instructions):
            self.records = sorted(
                self.records, 
                key=lambda r: str(r.get_value(field_name)).strip().lower()
                if field_name != "Count" 
                else int(r.get_value(field_name)) if str(r.get_value(field_name)).isdigit() else 0,
                reverse=descending
            )
        return True 
    def parse_sort_expression(self, text):

        """Parse a sort expression in the format "Field asc, Field2 desc".
        Args:       text (str): The sort expression to parse.                                       
        Returns:    Optional[List[SortInstruction]]: The parsed sort instructions as a list of (field, descending) tuples, or None if the expression is invalid.
        """
        if not text.strip():
            return None
        parts = [p.strip() for p in text.split(",") if p.strip()]
        instructions = []
        for part in parts:
            part_lower = part.lower()
            matched = False
            for field in FIELDS:
                f = field.lower()
                if part_lower == f:
                    instructions.append((field, False))
                    matched = True
                    break

                elif part_lower == f + " asc" or part_lower == f + " ascending":
                    instructions.append((field, False))
                    matched = True
                    break
                elif part_lower == f + " desc" or part_lower == f + " descending":
                    instructions.append((field, True))
                    matched = True
                    break
            if not matched:
                return None 
        return instructions
    def search_by_selected_fields(self, criteria: dict):
        results = []

        for index, record in enumerate(self.records): #Dhruv Sharma
            match = True

            for field, value in criteria.items():
                record_value = str(record.get_value(field)).lower()

                if value.lower() not in record_value: #Dhruv SHarma
                    match = False
                    break

            if match:
                results.append((index, record))
        return results