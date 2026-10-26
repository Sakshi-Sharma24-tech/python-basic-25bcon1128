"""
Program: Structure to Dictionary Conversion
Description: Demonstrates converting structured records (tuples, lists of tuples,
or class instances) into clean Python dictionaries.
"""

def tuple_list_to_dict(records):
    """
    Converts a list of (key, value) tuples into a dictionary.
    """
    return dict(records)

def student_record_to_dict(keys, values):
    """
    Combines keys and values into a dictionary mapping.
    """
    return dict(zip(keys, values))

if __name__ == "__main__":
    print("=== Structure to Dictionary Conversion ===")
    
    # Example 1: List of Tuples to Dictionary
    student_tuples = [("name", "Sakshi Sharma"), ("course", "B.Tech CSE"), ("year", 2)]
    student_dict = tuple_list_to_dict(student_tuples)
    print("\nConverted from list of tuples:")
    print(student_dict)

    # Example 2: Paired Keys & Values
    headers = ["roll_no", "subject", "marks", "grade"]
    data = [101, "Data Analytics", 95, "A+"]
    record_dict = student_record_to_dict(headers, data)
    print("\nConverted from parallel lists:")
    print(record_dict)
