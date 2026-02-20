"""
Author : Dhruv Sharma
Business Layer : in-memory list + CRUD
File name : record_service.py

"""

from typing import List, Optional
from model.record import Record
from persistence.csv_repository import CsvRepository

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
            self.records.pop(index)
            return True
        return False
    
        