# Student Grade Processing

def get_student_details(name, department, semester, m1, m2, m3):
    return {
        "name": name,
        "department": department,
        "semester": semester,
        "marks": [m1, m2, m3]
    }

def calculate_grade(marks):
    avg = sum(marks) / len(marks)

    if 90 <= avg <= 100:
        grade = "S"
    elif 80 <= avg <= 89:
        grade = "A"
    elif 65 <= avg <= 79:
        grade = "B"
    elif 50 <= avg <= 64:
        grade = "C"
    elif 40 <= avg <= 49:
        grade = "D"
    else:
        grade = "F"

    return avg, grade


if __name__ == "__main__":
    student = get_student_details("Sanjota", "CSE", 3, 85, 90, 88)
    avg, grade = calculate_grade(student["marks"])

    print("Student Name :", student["name"])
    print("Department   :", student["department"])
    print("Semester     :", student["semester"])
    print("Marks        :", student["marks"])
    print("Average      :", avg)
    print("Grade        :", grade)