student_heights = []

num_inputs = 10

print(f"Please enter the heights of {num_inputs} students:")

for i in range(num_inputs):
    height = int(input(f"Enter height for student {i + 1}: "))
    student_heights.append(height)

# Calculate the average height
average_height = sum(student_heights) / num_inputs

print("Average height of students:", average_height)
