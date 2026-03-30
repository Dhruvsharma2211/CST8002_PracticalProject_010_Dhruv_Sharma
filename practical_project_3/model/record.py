"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
File name : record.py
Description: This file defines model used to store one dataset row from the dataset. 
It also defines the dataset fields used throughout the application
Reference:
[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""
from dataclasses import dataclass
from typing import Dict, Any, List
# List [str]: Dataset colunm names used through tthe application
FIELDS: List[str] = [
    "Site identification",
    "Area",
    "Visit date",
    "Start time",
    "Species code",
    "Count",
]

@dataclass
class Record:
    """
    Represent a single dataset for record
    Attributes :
        Data (Dict) : Stores column  values pairs the record
    """
    data: Dict[str, Any]

    @staticmethod
    def empty() -> "Record":
        """
        Create an empty record with all required fields.
        Returns:
        Record: A new record with blank values for all fields.
        """
        return Record({field: ""for field in FIELDS})
    def get_value(self, field_name: str) -> Any:
        """
        Get a field value from the record.
        Args: 
         field_name(str): The dataset column name
         
         Returns:
         Any: The stored value for the field, or an empty string if missing
         """
        return self.data.get(field_name,"")