"""
Author : Dhruv Sharma
File name : main.py
Reference:
[1] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[2] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[3] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""

from practical_project_3.controller.record_controller import RecordController
from practical_project_3.business.record_service import RecordService
from practical_project_3.persistence.csv_repository import CsvRepository
from practical_project_3.presentation.cli_view import CliView

def main() -> None:
    dataset_path = "practical_project_2/" \
    "dataset/pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

    repo = CsvRepository(dataset_path=dataset_path)
    service = RecordService(repo=repo)
    controller = RecordController(service=service)
    view = CliView(controller=controller, full_name="Dhruv Sharma")

    view.run()

if __name__ == "__main__":
    main()