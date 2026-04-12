"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
File name : main.py
THis is the main entery point of the application. It initialixes all layers of MVC architeture and 
starts the CLI-bases program.
Reference:
[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
[7] 	Parks Canada, "Migratory Shorebird Habitat Use - Pacific Rim," open.canada.ca, 01 Oct 2017. [Online]. Available: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697. [Accessed 02 April 2026].
[8] 	www.geeksforgeeks.org, "Searching Algorithms in Python," www.geeksforgeeks.org, 04 Sep 2025. [Online]. Available: https://www.geeksforgeeks.org/dsa/searching-algorithms-in-python/. [Accessed 10 April 2026].
[9] 	R. Sharma, "Master Searching algorithms With Python in one shot," Medium.com, 21 June 2024. [Online]. Available: https://medium.com/pythoneers/master-searching-algorithms-with-python-in-one-shot-5f9eec198d43. [Accessed 12 04 2026].

"""

from practical_project_4.controller.record_controller import RecordController
from practical_project_4.business.record_service import RecordService
from practical_project_4.persistence.csv_repository import CsvRepository
from practical_project_4.presentation.cli_view import CliView

def main() -> None:
    dataset_path = "practical_project_4/" \
    "dataset/pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

    repo = CsvRepository(dataset_path=dataset_path)
    service = RecordService(repo=repo)
    controller = RecordController(service=service)
    view = CliView(controller=controller, full_name="Dhruv Sharma")

    view.run()

if __name__ == "__main__":
    main()