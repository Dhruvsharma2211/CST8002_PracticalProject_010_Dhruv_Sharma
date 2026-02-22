"""
Author : Dhruv Sharma
File name : record.py
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""
from dataclasses import dataclass
from typing import Dict, Any, List

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
    Stores one row from the dataset
    we keep a dict using the dataset column names as key.
    """
    data: Dict[str, Any]

    @staticmethod
    def empty() -> "Record":
        return Record({field: ""for field in FIELDS})
    