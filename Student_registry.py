import csv
import os

class StudentRegistry:
    def __init__(self, csv_file=r"D:\projects\School management\sampledata\students.csv"):
        self._students = {}         # Hash table for student data
        self._order = []            # Linked list to preserve order
        self.csv_file = csv_file    # File path
        self.load_from_csv()        # Load data automatically

    def load_from_csv(self):
        """Loads student data from a CSV file."""
        if not os.path.exists(self.csv_file):
            print(f"⚠️ File '{self.csv_file}' not found. Starting with empty registry.")
            return

        with open(self.csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Normalize header keys (strip whitespace and lowercase)
                row = {k.strip().lower(): v for k, v in row.items()}

                # Support both 'id' and 'student_id'
                sid = row.get('student_id') or row.get('id')
                if not sid:
                    print(f"⚠️ Skipping row (missing ID): {row}")
                    continue

                # Store normalized data internally
                row['student_id'] = sid
                self._students[sid] = row
                self._order.append(sid)

        print(f"✅ Loaded {len(self._students)} students from {self.csv_file}.")

    def save_to_csv(self):
        """Saves the current student data back to the CSV file."""
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['student_id', 'name', 'year', 'department']  # match your CSV
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sid in self._order:
                student = self._students[sid]
                writer.writerow({
                    'student_id': student['student_id'],
                    'name': student['name'],
                    'year': student['year'],
                    'department': student['department']
                })
        print(f"💾 Student data saved to {self.csv_file}.")

    def add_student(self, student):
        """Adds a new student and updates the CSV."""
        sid = student.get('student_id') or student.get('id')
        if sid in self._students:
            print(f"⚠️ Student with ID {sid} already exists — skipping.")
            return
        student['student_id'] = sid
        self._students[sid] = student
        self._order.append(sid)
        print(f"✅ Added student: {student['name']}")
        self.save_to_csv()

    def get_student(self, sid):
        """Retrieve a student by ID."""
        return self._students.get(sid)

    def remove_student(self, sid):
        """Remove a student and update CSV."""
        if sid in self._students:
            name = self._students[sid]['name']
            del self._students[sid]
            self._order.remove(sid)
            self.save_to_csv()
            print(f"🗑️ Removed student: {name}")
            return True
        print("⚠️ Student not found.")
        return False

    def iterate_students(self):
        """Loop through all students."""
        for sid in self._order:
            yield self._students[sid]


# --- Test Section ---
if __name__ == "__main__":
    registry = StudentRegistry(r"D:\projects\School management\sampledata\students.csv")

    print("\n--- Current Students ---")
    for student in registry.iterate_students():
        print(student)

    # Add a new student
    new_student = {
        "student_id": "106",
        "name": "Faith",
        "year": "1",
        "department": "Data Science"
    }
    registry.add_student(new_student)

    # Retrieve a student
    print("\n🔍 Searching for student 102...")
    student = registry.get_student("102")
    print(student if student else "Not found.")

    # Remove a student
    registry.remove_student("101")


