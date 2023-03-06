students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_attendances = 0
max_bonus_points = 0

for i in range(students):
    student_attendances = int(input())
    tot_bonus = student_attendances / lectures * (5 + additional_bonus)

    if student_attendances >= max_attendances:
        max_attendances = student_attendances
    if tot_bonus >= max_bonus_points:
        max_bonus_points = tot_bonus

print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {round(max_attendances)} lectures.")