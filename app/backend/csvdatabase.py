import csv
# CSV Database class
# Used to interact with CSV files like they are a database
class CSVDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_value(self, search_str, header):
        """Checks if a value exists under a given header."""
        if self.get_line_dic(search_str, header) == {}:
            return False
        return True


    def read_all(self):
        """Reads and returns all records from the CSV file as a list of dictionaries."""
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)


    def get_line_num(self, search_str, header):
        """
        Returns line number - 1 of row with search_str in the .csv file. Ignores header row.
        Ex: search_str = 'Hi' is on line 3, so 2 is returned.
        """
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                print(row)
                if row.get(header) == search_str:
                    return index

            return -1


    def get_line_dic(self, search_str, header):
        """
        Returns row with search_str in the .csv file. Ignores header row.
        """
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row[header] == search_str:
                    return row
            return {}


    def get_header_values(self, header):
        """
        Retrieves all values under a specified header as a list.
        """
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            if header not in reader.fieldnames:
                raise KeyError(f"Header '{header}' not found in {self.file_path}")
            return [row[header] for row in reader]

    def add_line(self, data):
        """Appends a new line to the CSV file. Data should be a dictionary matching the header names."""
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(data.keys()))
            writer.writerow(data)

    def remove_num_line(self, line_number):
        """Removes a line by line number (starting from 0 after the header) and rewrites the file."""
        records = self.read_all()
        if 0 <= line_number < len(records):
            del records[line_number]
            self.write_all(records)
        else:
            raise IndexError("Line number out of range.")

    def remove_str_line(self, search_str, header):
        """Removes a line by search_str. Ignores headers."""
        self.remove_num_line(self.get_line_num(search_str, header))

    def update_value(self, line_number, header, new_value):
        """Updates a specific value in the CSV file by line number and column name."""
        records = self.read_all()
        if 0 <= line_number < len(records):
            if header in records[line_number]:
                records[line_number][header] = new_value
                self.write_all(records)
            else:
                raise KeyError(f"Header '{header}' not found in {self.file_path}.")
        else:
            raise IndexError("Line number out of range.")

    def write_all(self, records):
        """Writes all records back to the CSV file."""
        if not records:
            raise ValueError(f"No records to write to {self.file_path}.")

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)

