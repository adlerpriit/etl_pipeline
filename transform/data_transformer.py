def transform_data(data):
    """
    Transforms a list of lists by converting all numerical values to floats.
    Assumes the input is a table of data, where each sub-list is a row.
    """
    transformed_data = []
    
    for row in data:
        new_row = []
        for value in row:
            try:
                new_row.append(float(value))
            except ValueError:
                new_row.append(value)
        transformed_data.append(new_row)
    
    return transformed_data

if __name__ == "__main__":
    data = [
        ["name", "age", "weight"],
        ["John Doe", "30", "75.5"],
        ["Jane Doe", "25", "68.2"],
    ]
    
    transformed_data = transform_data(data)
    for row in transformed_data:
        print(row)


import csv

def transform_and_write_data(data):
    transformed_data = []
    for row in data:
        new_row = []
        for value in row:
            try:
                new_row.append(float(value))
            except ValueError:
                new_row.append(value)
        transformed_data.append(new_row)
    
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transformed_data)

if __name__ == "__main__":
    data = [
        ["name", "age", "weight"],
        ["John Doe", "30", "75.5"],
        ["Jane Doe", "25", "68.2"],
    ]
    
    transform_and_write_data(data)
