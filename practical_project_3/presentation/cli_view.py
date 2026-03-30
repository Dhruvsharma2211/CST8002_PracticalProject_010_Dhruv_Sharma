"""
Course:  CST8002 - Programming Language Research
Author : Dhruv Sharma
Professor : Stanley Pieada
Due Date: 29th March 2026
Presentation Layer : Console menu
File Name : cli_view.py
This file implements command line interface for the application, It allows user
to perform CRUD operations, reload data, expoert data, and use the sorting feature.

Reference:

[1] 	w3schools.com, "Python List sort() Method," w3schools.com, N.A.. [Online]. Available: https://www.w3schools.com/python/ref_list_sort.asp. [Accessed 28 March 2026].
[2] 	A. Dalke and H. Raymond, "Sorting Techniques," docs.python.org, N.A.. [Online]. Available: https://docs.python.org/3/howto/sorting.html#ascending-and-descending. [Accessed 28 March 2026].
[3] 	T. Hunner, "Sorting iterables in Python," pythonmorsels.com, 07 May 2025. [Online]. Available: https://www.pythonmorsels.com/sorting-in-python/. [Accessed 28 March 2026].

[4] 	D. Hillard, "Effective Python Testing With pytest," realpython.com, 08 Dev 2024. [Online]. Available: https://realpython.com/pytest-python-testing/. [Accessed 22 02 2026].
[5] 	R. Oliveira, "GUID vs UUID vs ULID: Understanding Unique Identifiers," medium.com, 31 Jul 2024. [Online]. Available: https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13. [Accessed 22 Feb 2026].
[6] 	C. Team, "MVC Architecture Explained: Model, View, Controller," codecademy.com, N.D.. [Online]. Available: https://www.codecademy.com/article/mvc-architecture-model-view-controller. [Accessed 22 Feb 2026].
"""

from typing import Optional
from practical_project_3.controller.record_controller import RecordController
from practical_project_3.model.record import Record, FIELDS

class CliView: 
    def __init__(self, controller: RecordController, full_name: str) -> None:
        self.controller = controller
        self.full_name = full_name
    
    def _banner(self) -> None:
        print("\n" + "=" * 60)
        print(f"Program by {self.full_name}")
        print("=" * 60)

    def run(self) -> None:
        try:
            self.controller.init()
        except Exception as e:
            self._banner()
            print(f"Error loading dataset: {e}")
            input("Press Enter...")
            return
    
        while True:
            self._banner()
            print("1] Reload dataset (replace in memory data)")
            print("2] Export in-memory data to New CSV ")
            print("3] Display One Record")
            print("4] Display Multiple Records")
            print("5] Create New Record")
            print("6] Edit record")
            print("7] Delete a record")
            print("8] Sort records by column")
            print("0] Exit.....")
            choice = input("\n Choose an Option: ").strip()

            if choice == "1":
                self._reload()
        
            elif choice == "2":
                self._export()
        
            elif choice == "3":
                self._display_one()
            elif choice == "4":
                self._display_many()
            elif choice == "5":
                self._create()
            elif choice == "6":
                self._edit()
            elif choice =="7":
                self._delete()
            elif choice == "8":
                self._sort_records()
            elif choice == "0":
                self._banner()
                print("Bye See you next time..")
                break
            else:
                print("oops Invalid choice..")
                input("Press Enter")
    def _read_index(self) -> Optional[int]:
        raw = input("enter record index (0 Based): ").strip()
        return int(raw) if raw.isdigit() else None
    
    def _print_record(self, index: int, rec: Record) -> None:
        print("-" * 60)
        print(f"Record #{index}")
        for f in FIELDS:
            print(f"{f}: {rec.data.get(f, '')}")
        print("-" * 60)

    def _reload(self) -> None:
        try:
            self.controller.reload_data()
            print("Reloaded Dataset successfully")
        except Exception as e:
            print(f"Reload failed: {e}")
        input("Press Entet...")

    def _export(self) -> None:
        try:
            path = self.controller.export_data()
            print(f"Exported to: {path}")
        except Exception as e:
            print(f"Export Failed.. {e}")
        input("Press Enter")

    def _display_one(self) -> None:
        idx = self._read_index()
        if idx is None:
            print("Invalid Index...")
            input("Press Enter")
            return
        rec = self.controller.get_one(idx)
        if rec is None:
            print("Record not found")
        else: 
            self._print_record(idx, rec)
        input("Press Enter...")

    def _display_many(self) -> None:
        records = self.controller.get_all()
        if  not records:
            print("No records loadeed..")
            input("Press ENter")
            return
        raw = input("How many records you want to show? ").strip()
        if not raw.isdigit():
            print("Invalid number..")
            input("Press Enter..")
            return
        n = min(int(raw), len(records))

        for i in range(n):
            if i % 10 == 0:
                print(f"\n Program By {self.full_name} (records {i} to {min(i+9, n-1)})")
            self._print_record(i, records[i])
        
        input("Preess Enter..")

    def _create(self) -> None:
        rec = Record.empty()
        print("Enter Values for each field: ")
        for f in FIELDS:
            rec.data[f] = input(f"{f}: ").strip()
        self.controller.add(rec)
        print("Recprd added..")
        input("Press Enter..")

    def _edit(self) -> None:
        idx = self._read_index()
        if idx is None:
            print("Invalid Index..")
            input("Press Enter")
            return
        rec = self.controller.get_one(idx)
        if rec is None: 
            print("Record not found")
            input("press enter..")
            return
        new_rec = Record.empty()
        print("Press Enter to keep existing value.")
        for f in FIELDS:
            current = rec.data.get(f, "")
            new_val = input(f"{f} [{current}]: ").strip()
            new_rec.data[f] = new_val if new_val != "" else current
            
        print("Updated." if self.controller.edit(idx, new_rec) else "Update Failed")
        input("Enter PRess..")

    def _delete(self) -> None:
        idx = self._read_index()
        if idx is None:
            print("Invalid Index")
            print("Press Enter")
            return
        confirm = input("are you sure? (y/n): ").strip().lower()
        if confirm != "y":
            print("Canclled..")
            input("Press enter...")
            return
            
        print("Deleted." if self.controller.delete(idx) else "Delete Failed")
        input("Press Enter..")
    def _sort_records(self) -> None:
        print("\n Available fields for sorting")
        for index, field in enumerate(FIELDS, start=1):
            print(f"{index}] {field}")
        
        raw_field = input("Enter exect field name to sort by :").strip()
        order = input("ENter a for ascending or D to descending: ").strip().upper()
        descending = order == "D"

        success = self.controller.sort_records(raw_field, descending)
        if success:
            direction = "descending" if descending else "ascending"
            print(f"Records sorted by '{raw_field}' in {direction} order.")
        else:
            print("Sorting failed. Please enter a valid field name.")
        input("Press Enter to continue...")