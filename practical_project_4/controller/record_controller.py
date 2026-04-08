"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
Controller : connects view -> Business
File Name : record_controller.py
Controller
This File defines the controller layer that connects the user interface with the business logic layer. It handles requests from the view and passes them to the service layer.
It hanfdles requeest from the view and passes them to the service layer.

Reference:
[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""

from typing import List, Optional
from practical_project_4.model.record import Record
from practical_project_4.business.record_service import RecordService

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
    def sort_records(self, field_name: str, descending: bool = False) -> bool:
        return self.service.sort_records(field_name, descending)
    def sort_records_multi_from_text(self, text):
        instructions = self.service.parse_sort_expression(text) #Dhruv Sharma
        if instructions is None:
            return False
        
        return self.service.sort_records_multi(instructions)