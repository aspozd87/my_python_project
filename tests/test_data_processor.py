import unittest
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor('../data/sample_data.txt')

    def test_read_data(self):
        data = self.processor.read_data()
        self.assertEqual(len(data), 4)

    def test_get_ages(self):
        data = self.processor.read_data()
        ages = self.processor.get_ages(data)
        self.assertEqual(ages, [28, 24, 30, 22])

    def test_calculate_average_age(self):
        ages = [28, 24, 30, 22]
        average_age = self.processor.calculate_average_age(ages)
        self.assertEqual(average_age, 26)

if __name__ == '__main__':
    unittest.main()
