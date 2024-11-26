class student:
    def __init__ (self,name,scores):
        self.name = name
        self.scores = scores
    def calculate_average(self):
        return sum(self.scores)/len(self.scores)
    def is_passing(self,passing_score =40):
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        self.students = {}
    def add_student (self,name,scores):
        self.students[name] = student(name,scores)
    def calculate_class_average(self):
        total_scores = []
        for student in self.students.values():
            total_scores.extend(student.scores)
            return sum(total_scores)/len(total_scores) if total_scores else 0
    def display_student_performance(self):
        for name,student in self.students.items():
            average_score = student.calculate_average()
            passing_status = "Passing" if student.is_passing else "Failing"
            print(f"{name}: Average= {average_score:.2f} Status= {passing_status}")
            class_average = self.calculate_class_average()
            print(f"Class Average= {class_average:.2f}")
def main():
    tracker = PerformanceTracker()
    while True:
        student_name = input("Enter student name (or 'done' to finish): ").strip()
        if student_name.lower() == 'done':
            break
        scores = []
        subjects = ["Math", "Science", "English"]
        for subject in subjects:
            while True:
                try:
                    score = int(input(f"Enter {subject} score for {student_name}: "))
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        tracker.add_student(student_name, scores)
    tracker.display_student_performance()
if __name__ == "__main__":
    main()