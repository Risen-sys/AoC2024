#Commented Code is Part 1
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= diff <= 3 for diff in differences):
        return True
    if all(-3 <= diff <= -1 for diff in differences):
        return True

    return False

def safe_removal(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        alter_report = report[:i] + report[i+1:]
        if is_safe(alter_report):
            return True

    return False

def count_safe_reports_damp(filename):
    with open(filename, 'r') as file:
        reports = [[int(x) for x in line.split()] for line in file]

    safe_count = sum(safe_removal(report) for report in reports)
    return safe_count

"""
def count_safe_reports(filename):
    with open(filename, 'r') as file:
        reports = [[int(x) for x in line.split()] for line in file]

    safe_count = sum(is_safe(report) for report in reports)
    return safe_count
"""

filename = r'C:\Users\MatthewSilbernagel\Desktop\input.txt'
#safe_reports = count_safe_reports(filename)
#print(f"Number of safe reports: {safe_reports}")
count_safe_reports_damp = count_safe_reports_damp(filename)
print(f"Number of safe reports with Dampener: {count_safe_reports_damp}")