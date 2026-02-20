"""
Author : DHRUV SHarma
Pytest unit test : Check CSV load Works
"""

import csv
from persistence.csv_repository import CsvRepository
from model.record import FIELDS

def test_load_first_100_reads_records(tmp_path):
    csv_path = tmp_path / "test.csv"
    with csv_path.open("w", encoding="cp1252", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for i in range(3):
            writer.writerow({field: f"{field}_{i}" for field in FIELDS})

    repo = CsvRepository(dataset_path=str(csv_path))
    records = repo.load_first_100()

    assert len(records) == 3
    assert records[0].data[FIELDS[0]] == f"{FIELDS[0]}_0"