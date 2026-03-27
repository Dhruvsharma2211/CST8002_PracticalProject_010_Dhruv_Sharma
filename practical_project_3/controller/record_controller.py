"""
Author : DHRUV sharma
Controller : connects view -> Business
File Name : record_controller.py
Controller
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
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