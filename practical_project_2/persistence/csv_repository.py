"""
Author : Dhruv Sharma
 Persistence layer: CSV file input output + UUID export
File name : csv_repository.py
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].

"""

import csv
import uuid
from pathlib import Path
from typing import List

from practical_project_2.model.record import Record, FIELDS

class CsvRepository:
    def __init__(self, dataset_path: str) -> None:
        self.dataset_path = Path(dataset_path)
    def load_first_100(self) -> List[Record]:
        if not self.dataset_path.exists():
            raise FileNotFoundError(f"Dataset File not found: {self.dataset_path}")
        records: List[Record] = []
        #CSV is encoded cp1252
        with self.dataset_path.open("r", encoding="cp1252", newline="") as f:
            reader = csv.DictReader(f)

            header = reader.fieldnames or []

            missing_in_csv = [c for c in FIELDS if c not in header]
            missing_in_code = [c for c in header if c not in FIELDS]

            if missing_in_csv: 
                raise ValueError(f"CSV missing expected columns: {missing_in_csv}")
            if missing_in_code:
                raise ValueError(f"Your code  must include AlL dataset columns. Missing in FIELDS: {missing_in_code}")
            for i, row in enumerate(reader):
                if i >= 100:
                    break
                record_data = {field: row.get(field, "") for field in FIELDS}
                records.append(Record(record_data))
        return records
    
    def export_to_new_csv(self, records: List[Record], output_dir: str = "output") -> Path:
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{uuid.uuid4()}.csv" #Author : DHRUV SHARMA
        out_path = out_dir / filename

        with out_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for rec in records:
                writer.writerow({field: rec.data.get(field, "") for field in FIELDS})

        return out_path
    