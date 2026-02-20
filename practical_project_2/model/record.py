# Author : Dhruv Sharma
# File Name : record.py

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
    