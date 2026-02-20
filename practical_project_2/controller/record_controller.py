"""
Author : DHRUV sharma
Controller : connects view -> Business
File Name : record_controller.py
Controller
"""

from typing import List, Optional
from practical_project_2.model.record import Record
from practical_project_2.business.record_service import RecordService

class RecordController:
    def __init__(self, service: RecordService) -> None:
        self.service = service
    
    def init(self) -> None: 
        self.service.startup_load()
    
    def reload_data(self) -> None:
        self.service.reload()
    
    def export_data(self) -> str:
        return self.service.export()
        
    def get_all(self) -> List[Record]:
        return self.service.list_all()
    
    def get_one(self, index: int) -> Optional[Record]:
        return self.service.get_by_index(index)
    
    def add(self, record: Record) -> None:
        self.service.add(record)
    
    def edit(self, index: int, record: Record) -> bool:
        return self.service.update(index, record)
    
    def delete(self, index: int) -> bool:
        return self.service.delete(index)