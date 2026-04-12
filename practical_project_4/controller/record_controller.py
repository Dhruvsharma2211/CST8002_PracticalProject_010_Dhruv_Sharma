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
[7] 	Parks Canada, "Migratory Shorebird Habitat Use - Pacific Rim," open.canada.ca, 01 Oct 2017. [Online]. Available: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697. [Accessed 02 April 2026].
[8] 	www.geeksforgeeks.org, "Searching Algorithms in Python," www.geeksforgeeks.org, 04 Sep 2025. [Online]. Available: https://www.geeksforgeeks.org/dsa/searching-algorithms-in-python/. [Accessed 10 April 2026].
[9] 	R. Sharma, "Master Searching algorithms With Python in one shot," Medium.com, 21 June 2024. [Online]. Available: https://medium.com/pythoneers/master-searching-algorithms-with-python-in-one-shot-5f9eec198d43. [Accessed 12 04 2026].

"""

from typing import List, Optional
from practical_project_4.model.record import Record
from practical_project_4.business.record_service import RecordService


class RecordController:
    """Controller class that connects the view with the RecordService. It provides methods to handle user requests and interact with the business logic layer to manage records in memory, including loading data, adding, updating, deleting records, and sorting them based on specified fields.
    """

    def __init__(self, service: RecordService) -> None:
        """Initialize the RecordController with a RecordService instance.
        Args:      service (RecordService): The service instance to manage records.
        Returns:    None    
        """
        self.service = service

    def init(self) -> None:
        """Initialize the controller by loading the initial dataset into memory using the RecordService.
        Returns:      None
        """
        self.service.startup_load()

    def reload_data(self) -> None:
        """Reload the dataset, replacing the in-memory data with the first 100 records from the CSV file using the RecordService.
        Returns:      None  
        """
        self.service.reload()

    def export_data(self) -> str:
        """Export the current in-memory records to a new CSV file with a UUID filename using the RecordService.
        Returns:      str: The file path of the exported CSV file.
        """
        return self.service.export()

    def get_all(self) -> List[Record]:
        """Get a list of all records currently in memory using the RecordService.
        Returns:      List[Record]: A list of all records currently stored in memory.
        """
        return self.service.list_all()

    def get_one(self, index: int) -> Optional[Record]:
        """Get a single record by its index in the in-memory list using the RecordService.
        Args:      index (int): The index of the record to retrieve.            
        Returns:    Optional[Record]: The record at the specified index, or None if the index is out of range.
        """
        return self.service.get_by_index(index)

    def add(self, record: Record) -> None:
        """Add a new record to the in-memory list using the RecordService.
        Args:      record (Record): The record to add to the in-memory list.
        """
        self.service.add(record)

    def edit(self, index: int, record: Record) -> bool:
        """Edit an existing record in the in-memory list using the RecordService.
        Args:      index (int): The index of the record to update.
               record (Record): The new record data to replace the existing record.
        Returns:      bool: True if the update is successful, otherwise False.
        """
        return self.service.update(index, record)

    def delete(self, index: int) -> bool:
        """Delete a record from the in-memory list using the RecordService.
        Args:      index (int): The index of the record to delete.  
        Returns:      bool: True if the deletion is successful, otherwise False.
        """
        return self.service.delete(index)

    def sort_records(self, field_name: str, descending: bool = False) -> bool:
        """Sort the in-memory records by a specified field using the RecordService.
        Args:      field_name (str): The name of the field to sort by.
               descending (bool): Whether to sort in descending order (default is False for ascending). 
        Returns:      bool: True if the sorting is successful, otherwise False.
        """
        return self.service.sort_records(field_name, descending)

    def sort_records_multi_from_text(self, text: str) -> bool:
        """
        Sort the in-memory records by multiple fields based on a text input using the RecordService.
        Args:      text (str): A text input specifying the sort fields and order (e.g., "Area desc, Visit date asc").
        Returns:      bool: True if the sorting is successful, otherwise False.
        """
        instructions = self.service.parse_sort_expression(text)  # Dhruv Sharma
        if instructions is None:
            return False

        return self.service.sort_records_multi(instructions)


    def search_by_selected_fields(self, criteria: dict):
        return self.service.search_by_selected_fields(criteria) #Dhruv Sharma