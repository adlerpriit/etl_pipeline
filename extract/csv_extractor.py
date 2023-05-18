import csv

def extract_data(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    extract_data('data.csv')