student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_scores[student] = "Outstanding"

    elif 81 <= score <= 90:
        student_scores[student] = "Exceeds Expectations"

    elif 71 <= score <= 80:
        student_scores[student] = "Acceptable"
        
    elif score <= 70:
        student_scores[student] = "Failed"

print("Student Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

