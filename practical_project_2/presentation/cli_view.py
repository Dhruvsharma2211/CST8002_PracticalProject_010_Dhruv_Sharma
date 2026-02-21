"""
Author : DHRuv SHarma

Presentation Layer : Console menu
File Name : cli_view.py
"""

from typing import Optional
from practical_project_2.controller.record_controller import RecordController
from practical_project_2.model.record import Record, FIELDS

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
