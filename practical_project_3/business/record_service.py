"""
Author : Dhruv Sharma
Business Layer : in-memory list + CRUD
File name : record_service.py
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].

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
        