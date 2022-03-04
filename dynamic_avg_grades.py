count = int(input("How much grades to you want to inform? "))
grades = []

for i in range(count):
  grade = float(input(f"Inform your {i + 1}° grade: "))
  grades.append(grade)

def calc_average_grade(grades):
  sum = 0

  for i in grades:
    sum += i

  return sum / len(grades)

print(f"You average grades: {calc_average_grade(grades)}")
