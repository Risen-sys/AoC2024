from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate the expression given numbers and operators left-to-right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def parse_input(input_data):
    """Parse the input data into test values and lists of numbers."""
    equations = []
    for line in input_data.strip().split("\n"):
        if ":" not in line:
            continue  # Skip lines without a colon
        try:
            test_value, nums = line.split(":")
            test_value = int(test_value.strip())
            numbers = list(map(int, nums.strip().split()))
            equations.append((test_value, numbers))
        except ValueError:
            continue  # Skip lines that cannot be parsed correctly
    return equations

def find_calibration_result(input_data):
    """Determine the total calibration result."""
    equations = parse_input(input_data)
    total = 0

    for test_value, numbers in equations:
        num_operators = len(numbers) - 1
        if num_operators == 0:
            # Single number case
            if numbers[0] == test_value:
                total += test_value
            continue

        # Dynamically build expressions and check efficiently
        stack = [(numbers[0], 0)]  # (current_value, operator_index)

        while stack:
            current, index = stack.pop()

            if index == num_operators:
                if current == test_value:
                    total += test_value
                    break
                continue

            # Add next operator
            next_num = numbers[index + 1]
            stack.append((current + next_num, index + 1))
            stack.append((current * next_num, index + 1))
            stack.append((int(str(current) + str(next_num)), index + 1))

    return total

# Read input from file
file_path = r"C:\Users\MatthewSilbernagel\Desktop\input.txt"
with open(file_path, 'r') as file:
    data = file.read()

# Find and print the total calibration result
result = find_calibration_result(data)
print("Total Calibration Result:", result)
