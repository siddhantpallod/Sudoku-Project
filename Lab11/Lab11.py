import os
import matplotlib.pyplot as plt

def load_students(file_name):
    students = {}
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            student_id = line[:3]
            student_name = line[3:].strip()

            students[student_id] = student_name
    return students

def load_assignments(file_name):
    assignments = {}
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            assignment_name = lines[i].strip()
            assignment_id = lines[i+1].strip()
            points = int(lines[i+2].strip())

            assignments[assignment_id] = (assignment_name, points)

    return assignments

def load_submissions(folder_name):
    submissions = {}
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        if not os.path.isfile(file_path):
            continue
        with open(file_path, 'r') as f:
            for line in f:
                student_id, assignment_id, percentage = line.strip().split('|')
                if student_id not in submissions:
                    submissions[student_id] = []
                submissions[student_id].append((assignment_id, int(percentage)))
    return submissions

def calculate_student_grade(student_name, students, assignments, submissions):
    student_id = None

    for sid, name in students.items():
        if name == student_name:
            student_id = sid
            break

    if not student_id:
        print("Student not found")
        return

    total_points = 0
    total_possible = 1000

    for assignment_id, percentage in submissions.get(student_id, []):
        assignment_name, points = assignments.get(assignment_id, (None, 0))
        if assignment_name:
            total_points += (percentage / 100) * points

    grade_percentage = round((total_points / total_possible) * 100)
    print(f"{grade_percentage}%")

def assignment_stats(assignment_name, assignments, submissions):
    assignment_id = None
    for aid, (name, _) in assignments.items():
        if name == assignment_name:
            assignment_id = aid
            break
    if not assignment_id:
        print("Assignment not found")
        return
    all_scores = []
    for student_submissions in submissions.values():
        for sid, percent in student_submissions:
            if sid == assignment_id:
                all_scores.append(percent)

    if not all_scores:
        print("No submissions found for this assignment")
        return

    min_score = min(all_scores)
    max_score = max(all_scores)
    avg_score = sum(all_scores) / len(all_scores)

    print(f"Min: {min_score}%")
    print(f"Avg: {round(avg_score)}%")
    print(f"Max: {max_score}%")

def assignment_graph(assignment_name, assignments, submissions):
    assignment_id = None
    for aid, (name, _) in assignments.items():
        if name == assignment_name:
            assignment_id = aid
            break
    if not assignment_id:
        print("Assignment not found")
        return

    all_scores = []
    for student_submissions in submissions.values():
        for sid, percent in student_submissions:
            if sid == assignment_id:
                all_scores.append(percent)

    if not all_scores:
        print("No submissions found for this assignment")
        return

    plt.hist(all_scores, bins=[0, 25, 50, 75, 100])
    plt.xlabel('Score (%)')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of scores for {assignment_name}')
    plt.show()

def main():
    students = load_students('data/data/students.txt')
    assignments = load_assignments('data/data/assignments.txt')
    submissions = load_submissions('data/data/submissions')

    while True:
        print("1: Student grade")
        print("2: Assignment statistics")
        print("3: Assignment graph")

        selection = input("Enter your selection: ")

        if selection == "1":
            student_name = input("What is the student's name: ")
            calculate_student_grade(student_name, students, assignments, submissions)

        elif selection == "2":
            assignment_name = input("What is the assignment name: ")
            assignment_stats(assignment_name, assignments, submissions)

        elif selection == "3":
            assignment_name = input("What is the assignment name: ")
            assignment_graph(assignment_name, assignments, submissions)

        break

if __name__ == "__main__":
    main()