
#Course CST8002 - Programming Language Research Project
#Professor : Stanley Pieda
#Due Date : 1st Feb 2026
#Author : Dhruv Sharma 
# File name: record.py
# This file defines the record object(Entity / Data transfer object)

class Record:
    def __init__(self, site_identification, area, visit_date, start_time, species_code, count):

        # Variables based directly on csv columm names
        self.site_identification = site_identification
        self.area = area
        self.visit_date = visit_date
        self.start_time = start_time
        self.species_code = species_code
        self.count = count

        # getters

    def get_site_identification(self):
            return self.site_identification
        
    def get_area(self):
            return self.area
        
    def get_visit_date(self):
            return self.visit_date
        
    def get_start_time(self):
            return self.start_time
        
    def get_species_code(self):
            return self.species_code
        
    def get_count(self):
            return self.count
        
        # Setters

    def set_site_identification(self, value):
            self.site_identification = value
        
    def set_area(self, value):
            self.area = value
        
    def set_visit_date(self, value):
            self.visit_date = value
        
    def set_start_time(self, value):
            self.start_time = value
        
    def set_species_code(self, value):
            self.species_code = value

    def set_count(self, value):
            self.count = value

    # string output for showing records data 
    def __str__(self):
        return (
            f"Site: {self.site_identification},"
            f"Area: {self.area},"
            f"Visit_Date: {self.visit_date},"
            f"Start_Time: {self.start_time},"
            f"Species: {self.species_code},"
            f"Count: {self.count}"

        )


