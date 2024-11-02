import csv

class CSVDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_all(self):
        """Reads and returns all records from the CSV file as a list of dictionaries."""
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def read_line(self, search_str):
        """
        Searches for a line containing the str in any column and returns the first matching line
        and the corresponding line number. Ignores the header row.
        """
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                if any(search_str in str(value) for value in row.values()):
                    return row, index
            raise ValueError(f"'{search_str}' not found in {self.file_path}")

    def get_row_num(self, search_str):
        """
        Returns line number - 1 of row with search_str in the .csv file. Ignores header row.
        Ex: search_str = 'Hi' is on line 3, so 2 is returned.
        """
        return self.read_line(search_str)[1]

    def get_row(self, search_str):
        """
        Returns row with search_str in the .csv file. Ignores header row.
        """
        return self.read_line(search_str)[0]

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
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writerow(data)

    def remove_num_line(self, line_number):
        """Removes a line by line number (starting from 0 after the header) and rewrites the file."""
        records = self.read_all()
        if 0 <= line_number < len(records):
            del records[line_number]
            self.write_all(records)
        else:
            raise IndexError("Line number out of range.")

    def remove_str_line(self, search_str):
        """Removes a line by search_str. Ignores headers."""
        self.remove_num_line(self.get_row_num(search_str))

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

