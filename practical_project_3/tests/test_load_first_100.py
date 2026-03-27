"""
Author : DHRUV SHarma
Pytest unit test : Check CSV load Works
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""

import csv
from practical_project_2.persistence.csv_repository import CsvRepository
from practical_project_2.model.record import FIELDS

def test_load_first_100_reads_records(tmp_path):
    print("\n Author: DHRUV SHARMA | CST8002 Practical Project2")
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
    