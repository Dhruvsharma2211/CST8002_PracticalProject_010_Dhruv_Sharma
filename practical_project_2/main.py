# Author : Dhruv Sharma
#File Name: main.py

from practical_project_2.controller.record_controller import RecordController
from practical_project_2.business.record_service import RecordService
from practical_project_2.persistence.csv_repository import CsvRepository
from practical_project_2.presentation.cli_view import CliView

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