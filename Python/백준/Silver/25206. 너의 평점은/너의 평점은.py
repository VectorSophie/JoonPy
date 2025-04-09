grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

arr = []
total = 0.0
def gradegpt(p, g):
    p = float(p)
    if g in grade_dict:
        arr.append(grade_dict[g] * p)
        return p
    return 0
for i in range(20):
    classe, point, grade = input().split()
    if grade != 'P':
        total += gradegpt(point, grade)
gpa = sum(arr) / total
print(f"{gpa:.10f}")