# Author : Dhruv Sharma
#File Name: main.py

from practical_project_2.controller.record_controller import StudentController
from practical_project_2.business.record_service import StudentService
from persistence.csv_repository import CsvRepository
from presentation.cli_view import CliView

def main() -> None:
    dataset_path = "dataset/pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

    repo = CsvRepository(dataset_path=dataset_path)
    service = StudentService(repo=repo)
    controller = StudentController(service=service)
    view = CliView(controller=controller, full_name="Dhruv Sharma")

    view.run()

if __name__ == "__main__":
    main()