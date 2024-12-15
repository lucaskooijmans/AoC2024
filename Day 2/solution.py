def read_reports(file_path):
    with open(file_path, 'r') as file:
        reports = [list(map(int, line.strip().split())) for line in file]
    return reports

def is_safe_report(report):
    # Check if the report is all increasing or all decreasing
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe_with_dampener(report):
    # Check if removing a single level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the ith level
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports(reports):
    safe_count = sum(1 for report in reports if is_safe_report(report))
    return safe_count

def count_safe_reports_with_dampener(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report) or can_be_safe_with_dampener(report):
            safe_count += 1
    return safe_count

reports = read_reports("input.txt")

# Part One
safe_report_count = count_safe_reports(reports)
print("Number of safe reports:", safe_report_count)

# Part Two
safe_report_count_with_dampener = count_safe_reports_with_dampener(reports)
print("Number of safe reports with dampener:", safe_report_count_with_dampener)