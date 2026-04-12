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
from practical_project_4.controller.record_controller import RecordController
from practical_project_4.model.record import Record, FIELDS

class CliView: 
    """Command-line interface view class that interacts with the user and communicates with the RecordController to perform various operations on the records, including displaying, creating, editing, deleting, sorting, and searching records in memory.
    """
    def __init__(self, controller: RecordController, full_name: str) -> None:
        """Initialize the CliView with a RecordController instance and the full name of the program author.
        Args:      controller (RecordController): The controller instance to manage records.        
            full_name (str): The full name of the program author to display in the banner.
            Returns:      None
        """
        self.controller = controller
        self.full_name = full_name
    
    def _banner(self) -> None:
        """Display a banner with the program author's name at the top of the console interface.
        Returns:      None
        """
        print("\n" + "=" * 60)
        print(f"Program by {self.full_name}")
        print("=" * 60)

    def run(self) -> None:
        """Run the main loop of the CLI view, displaying a menu of options to the user and handling their input to perform various operations on the records using the RecordController.
        Returns:      None  
        """
        try:
            self.controller.init()
        except Exception as e:
            self._banner()
            print(f"Error loading dataset: {e}")
            input("Press Enter...")
            return
    
        while True:
      
            self._banner()
            """Display the main menu options to the user.
            The menu includes options to reload the dataset, export data to a new CSV file, display one or multiple records, create a new record, edit an existing record, delete a record, and sort records by column(s). The user can choose an option by entering the corresponding number."""
            print("1] Reload dataset (replace in memory data)")
            print("2] Export in-memory data to New CSV ")
            print("3] Display One Record")
            print("4] Display Multiple Records")
            print("5] Create New Record")
            print("6] Edit record")
            print("7] Delete a record")
            print("8] Sort records by one column")
            print("9] Sort records by Multiple columns")
            print("10] Search/Filter records by multiple columns") #New Feature (DhruvSharma)
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
            elif choice == "9":
                self._sort_records()
            elif choice == "10":
                self._search_multiple_fields()
            elif choice == "0":
                self._banner()
                print("Bye See you next time..")
                break
            else:
                print("oops Invalid choice..")
                input("Press Enter")
    def _read_index(self) -> Optional[int]:
        """Read a record index from user input and validate it. 
            The method prompts the user to enter a record index (0-based) and checks if the input is a valid integer. If the input is valid, it returns the index as an integer; otherwise, it returns None.
            Returns:      Optional[int]: The record index entered by the user, or None if the input is invalid.
        """
        raw = input("enter record index (0 Based): ").strip()
        return int(raw) if raw.isdigit() else None
    
    def _print_record(self, index: int, rec: Record) -> None:
        """
        Print the details of a single record to the console in a formatted manner.
        Args:      index (int): The index of the record to display. 
                rec (Record): The record object containing the data to display.
        """
        print("-" * 60)
        print(f"Record #{index}")
        for f in FIELDS:
            print(f"{f}: {rec.data.get(f, '')}")
        print("-" * 60)

    def _reload(self) -> None:
        """Reload the dataset by calling the reload_data method of the RecordController. This method replaces the in-memory data with the first 100 records from the CSV file. If the reload is successful, it prints a success message; otherwise, it catches any exceptions and prints an error message.
        """
        try:
            self.controller.reload_data()
            print("Reloaded Dataset successfully")
        except Exception as e:
            print(f"Reload failed: {e}")
        input("Press Entet...")

    def _export(self) -> None:
        """Export the current in-memory records to a new CSV file by calling the export_data method of the RecordController. This method attempts to export the data and prints the file path of the exported CSV file if successful. If any exceptions occur during the export process, it catches them and prints an error message.
        """
        try:
            path = self.controller.export_data()
            print(f"Exported to: {path}")
        except Exception as e:
            print(f"Export Failed.. {e}")
        input("Press Enter")

    def _display_one(self) -> None:
        """Display a single record based on user input. The method prompts the user to enter a record index, retrieves the corresponding record using the RecordController, and prints the record details to the console. If the index is invalid or the record is not found, it prints an appropriate message. 
        """
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
        """
        Display multiple records to the console. The method retrieves all records currently in memory using the RecordController and prompts the user to enter how many records they want to display. It then prints the specified number of records in a formatted manner. If there are no records loaded or if the user enters an invalid number, it prints an appropriate message.
        """
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
        """
        Create a new record by prompting the user to enter values for each field. The method initializes an empty record and iterates through the predefined fields, asking the user to input a value for each field. The entered values are stored in the record's data dictionary. After all fields have been filled, the new record is added to the in-memory list using the RecordController, and a success message is printed.
        """
        rec = Record.empty()
        print("Enter Values for each field: ")
        for f in FIELDS:
            rec.data[f] = input(f"{f}: ").strip()
        self.controller.add(rec)
        print("Recprd added..")
        input("Press Enter..")

    def _edit(self) -> None:
        """
        Edit an existing record by prompting the user to enter a record index and new values for each field. The method first reads a record index from the user and retrieves the corresponding record using the RecordController. If the index is valid and the record is found, it initializes a new empty record and prompts the user to enter new values for each field, allowing them to press Enter to keep the existing value. The updated record is then saved using the RecordController's edit method, and a success or failure message is printed based on the result.
        """
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
        """Delete a record by prompting the user to enter a record index. The method reads a record index from the user and asks for confirmation before deleting the record. If the user confirms, it calls the delete method of the RecordController to remove the record from the in-memory list and prints a success or failure message based on the result. If the index is invalid, it prints an appropriate message.
        """
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
        """Sort the in-memory records by a specified field. The method displays the available fields for sorting and prompts the user to enter a sort expression (e.g., "Area asc" or "Count desc"). It then calls the sort_records_multi_from_text method of the RecordController to perform the sorting based on the user's input. If the sorting is successful, it prints a success message; otherwise, it prints an error message indicating that the sorting failed.
        """
        print("\n Available fields for sorting")
        for index, field in enumerate(FIELDS, start=1):
            print(f"{index}] {field}")
        text = input("Enter sort (example: Area asc, Count desc):")
        success = self.controller.sort_records_multi_from_text(text)
        if success:
            print("Records sorted successfully.")
        else:
            print("Sorting failed. Please enter a valid field name.")
        input("Press Enter to continue...")
    def _search_multiple_fields(self) -> None:


        print("\nSelect columns to search (comma separated):")

        valid_fields = {
            1: "Site identification",
            2: "Area",
            3: "Visit date",
            5: "Species code",
            6: "Count"
        }

        for num, field in valid_fields.items():
            print(f"{num}] {field}")

        selected = input("\nEnter column numbers (e.g. 1,2,5): ").strip()

        if not selected:
            print("No selection made.")
            input("Press Enter...")
            return

        try:
            selected_nums = [int(x.strip()) for x in selected.split(",")]
        except ValueError:
            print("Invalid input.")
            input("Press Enter...")
            return

        criteria = {}


        for num in selected_nums:
            if num not in valid_fields:
                print(f"Invalid column: {num}")
                input("Press Enter...")
                return

            field_name = valid_fields[num]


            value = input(f"Enter value for {field_name}: ").strip()

            if value == "":
                print("Empty value not allowed.")
                input("Press Enter...")
                return

            criteria[field_name] = value


        results = self.controller.search_by_selected_fields(criteria)

        if not results:
            print("\nNo matching records found.")
            input("Press Enter...")
            return

        print(f"\nFound {len(results)} matching record(s):")

        for index, record in results:
            self._print_record(index, record)

        input("Press Enter...")