def main():
    num_students = 5
    num_subjects = 5

    students = []

    for i in range(num_students):
        student_name = input(f"Enter name of student {i + 1}: ")
        total_marks = sum(float(input(f"Enter mark for subject {j + 1} of {student_name}: ")) for j in range(num_subjects))
        students.append((student_name, total_marks))

    print("\nStudent Name \t Total Marks")
    print("--------------------------------")
    for student in students:
        print(f"{student[0]} \t\t {student[1]}")

if __name__ == "__main__":
    main()
