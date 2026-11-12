def calculate_total(test1, test2, assignment):
    # Check whether all marks are between 0 and 100
    if test1 < 0 or test1 > 100:
        return None
    if test2 < 0 or test2 > 100:
        return None
    if assignment < 0 or assignment > 100:
        return None

    # Calculate weighted marks
    total = (test1 * 0.30) + (test2 * 0.30) + (assignment * 0.40)
    return total


def assign_grade(total):
    if total >= 90:
        return "A"
    elif total >= 80:
        return "B"
    elif total >= 70:
        return "C"
    elif total >= 60:
        return "D"
    elif total >= 40:
        return "E"
    else:
        return "F"


def check_pass_status(total):
    if total >= 40:
        return "Pass"
    else:
        return "Fail"
