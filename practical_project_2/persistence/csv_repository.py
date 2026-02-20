"""
Author : Dhruv Sharma
 Persistence layer: CSV file input output + UUID export
File name : csv_repository.py
"""

import csv
import uuid
from pathlib import Path
from typing import List

from model.record import Record, FIELDS

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

        filename = f"{uuid.uuid4()}.csv"
        out_path = out_dir / filename

        with out_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for rec in records:
                writer.writerow({field: rec.data.get(field, "") for field in FIELDS})

        return out_path
    