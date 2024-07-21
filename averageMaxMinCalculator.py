student_scores = []

num_inputs = 10

print(f"Please enter the score of {num_inputs} students:")

for i in range(num_inputs):
    score = int(input(f"Enter score for student {i + 1}: "))
    student_scores.append(score)

average_score = sum(student_scores) / num_inputs
highest_score = max(student_scores)
minimum_score = min(student_scores)

print("Average score of students:", average_score)
print("Highest score of students:", highest_score)
print("Minimum score of students:", minimum_score)