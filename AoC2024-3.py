import re
"""Part 1
def calc_sum(filepath):
    with open(filepath, "r") as file:
        corrupted_mem = file.read()


    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    matches = re.findall(pattern, corrupted_mem)

    result_sum = sum(int(x) * int(y) for x, y in matches)
    return result_sum
"""
def calc_cond_sum(filepath):
    with open(filepath, "r") as file:
        corrupted_mem = file.read()

    mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    mul_enabled = True
    result_sum = 0

    tokens = re.split(r"(?=mul\(|do\(\)|don't\(\))", corrupted_mem)

    for token in tokens:
        if re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled and re.match(mul_pattern, token):
            x, y = map(int, re.findall(mul_pattern, token)[0])
            result_sum += x * y

    return result_sum
    
filepath = r'C:\Users\MatthewSilbernagel\Desktop\input.txt'

try:
    result = calc_cond_sum(filepath)
    print("the sum of valid multiplications is:", result)
except FileNotFoundError:
    print(f"The file '{filepath}' was not found. Please ensure it exists.")
