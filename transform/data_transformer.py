def transform_data(data):
    """
    Transforms a list of lists by converting all numerical values to floats.
    Assumes the input is a table of data, where each sub-list is a row.
    """
    transformed_data = []
    #Adding test comment
    #Test comment
    #BRANCH COMMENT1

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

def standardize_data(data):
    """
    Standardizes numerical data to have a mean of 0 and standard deviation of 1.
    Assumes the input is a table of data, where each sub-list is a row.
    """
    # Get all numerical values
    numerical_values = [value for row in data[1:] for value in row if isinstance(value, float)]
    
    # Calculate the mean and standard deviation
    mean = sum(numerical_values) / len(numerical_values)
    std_dev = (sum((x - mean) ** 2 for x in numerical_values) / len(numerical_values)) ** 0.5
    
    # Create a new table with standardized numerical values
    standardized_data = []
    for row in data:
        new_row = []
        for value in row:
            if isinstance(value, float):
                new_value = (value - mean) / std_dev
                new_row.append(new_value)
            else:
                new_row.append(value)
        standardized_data.append(new_row)
    
    return standardized_data

if __name__ == "__main__":
    data = [
        ["name", "age", "weight"],
        ["John Doe", "30", "75.5"],
        ["Jane Doe", "25", "68.2"],
    ]
    
    transformed_data = transform_data(data)
    standardized_data = standardize_data(transformed_data)
    for row in standardized_data:
        print(row)