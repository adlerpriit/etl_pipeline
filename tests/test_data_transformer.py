import unittest
from data_transformer import transform_data

class TestDataTransformer(unittest.TestCase):
    
    def test_transform_data(self):
        # Define the input and expected output
        input_data = [
            ["name", "age", "weight"],
            ["John Doe", "30", "75.5"],
            ["Jane Doe", "25", "68.2"],
        ]

        expected_output = [
            ["name", "age", "weight"],
            ["John Doe", 30.0, 75.5],
            ["Jane Doe", 25.0, 68.2],
        ]

        # Call the function with the test input
        actual_output = transform_data(input_data)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
