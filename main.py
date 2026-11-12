from marks_pkg import calculate_total, assign_grade, check_pass_status

print("INTERNAL MARKS CALCULATOR")

test1 = float(input("Enter Test 1 marks: "))
test2 = float(input("Enter Test 2 marks: "))
assignment = float(input("Enter Assignment marks: "))

total = calculate_total(test1, test2, assignment)

if total is None:
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    grade = assign_grade(total)
    status = check_pass_status(total)

    print("\n----- RESULT -----")
    print("Total Marks:", round(total, 2))
    print("Grade:", grade)
    print("Status:", status)
