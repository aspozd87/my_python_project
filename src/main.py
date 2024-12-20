from data_processor import DataProcessor

def main():
    processor = DataProcessor('../data/sample_data.txt')
    data = processor.read_data()
    ages = processor.get_ages(data)
    average_age = processor.calculate_average_age(ages)
    print(f"Average age: {average_age}")

if __name__ == "__main__":
    main()
