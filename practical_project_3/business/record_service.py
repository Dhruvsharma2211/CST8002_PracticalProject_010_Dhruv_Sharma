"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
Business Layer : in-memory list + CRUD
File name : record_service.py
This file contains the business logic of the application including CRUD operation and sorting algorithm implemented for the project 3.
Reference:

[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""

from typing import List, Optional
from practical_project_3.model.record import Record, FIELDS
from practical_project_3.persistence.csv_repository import CsvRepository

class RecordService:
    def __init__(self, repo: CsvRepository) -> None:
        self.repo = repo
        self.records: List[Record] = []

    def startup_load(self) -> None:
        self.records = self.repo.load_first_100()
    
    def reload(self) -> None:
        self.records = self.repo.load_first_100()

    def export(self) -> str:
        return str(self.repo.export_to_new_csv(self.records))
    
    def list_all(self) -> List[Record]:
        return self.records

    def get_by_index(self, index: int) -> Optional[Record]:
        if 0 <= index < len(self.records):
            return self.records[index]
        return None
    def add(self, record: Record) -> None:
        self.records.append(record)
    
    def update(self, index: int, record: Record) -> bool:
        if 0 <= index < len(self.records):
            self.records[index] = record
            return True
        return False
    
    def delete(self, index: int) -> bool:
        if 0 <= index < len(self.records):
            self.records.pop(index)
            return True
        return False
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
        