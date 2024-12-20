class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, 'r') as file:
            data = file.readlines()
        return [line.strip().split(', ') for line in data]

    def get_ages(self, data):
        return [int(row[2]) for row in data]

    def calculate_average_age(self, ages):
        return sum(ages) / len(ages)
