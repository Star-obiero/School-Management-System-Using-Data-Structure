import csv
import os
from collections import deque

class Course:
    def __init__(self, course_id, name, capacity):
        self.id = course_id
        self.name = name
        self.capacity = int(capacity)
        self.enrolled = set()
        self.waitlist = deque()  # Queue to preserve registration order

    def enroll(self, sid):
        """Enroll a student or add them to the waitlist if full."""
        if len(self.enrolled) < self.capacity:
            self.enrolled.add(sid)
            print(f"✅ Student {sid} enrolled in {self.id}")
            return "enrolled"
        else:
            if sid not in self.waitlist:
                self.waitlist.append(sid)
                print(f"🕒 Course full — {sid} added to waitlist for {self.id}")
            else:
                print(f"⚠️ {sid} is already on waitlist for {self.id}")
            return "waitlisted"

    def drop_student(self, sid):
        """Drop a student and move next from waitlist if available."""
        if sid in self.enrolled:
            self.enrolled.remove(sid)
            print(f"🗑️ Student {sid} dropped from {self.id}")
            self.process_waitlist()
            return True
        elif sid in self.waitlist:
            self.waitlist.remove(sid)
            print(f"🗑️ Student {sid} removed from waitlist for {self.id}")
            return True
        else:
            print(f"⚠️ Student {sid} not found in {self.id}")
            return False

    def process_waitlist(self):
        """Move next student from waitlist to enrolled if space opens."""
        while len(self.enrolled) < self.capacity and self.waitlist:
            next_sid = self.waitlist.popleft()
            self.enrolled.add(next_sid)
            print(f"✅ Waitlisted student {next_sid} moved to enrolled in {self.id}")


class CourseScheduler:
    def __init__(self, csv_file=r"D:\projects\School management\sampledata\course.csv"):
        self.csv_file = csv_file
        self.courses = {}
        self.load_from_csv()

    def load_from_csv(self):
        """Loads all courses from CSV file."""
        if not os.path.exists(self.csv_file):
            print(f"⚠️ File '{self.csv_file}' not found. Starting with empty course list.")
            return

        with open(self.csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Match your CSV column names
                course_id = row['course_code']
                name = row['course_name']
                capacity = row['capacity']

                course = Course(course_id, name, capacity)

                # Load enrolled students
                enrolled_list = row['enrolled_students'].split('|') if row['enrolled_students'] else []
                for sid in enrolled_list:
                    sid = sid.strip()
                    if sid:
                        course.enrolled.add(sid)

                # Waitlist column (optional)
                if 'waitlist' in row and row['waitlist']:
                    waitlist_list = row['waitlist'].split('|')
                    for sid in waitlist_list:
                        sid = sid.strip()
                        if sid:
                            course.waitlist.append(sid)

                self.courses[course.id] = course

        print(f"✅ Loaded {len(self.courses)} courses from {self.csv_file}.")

    def save_to_csv(self):
        """Saves all courses to CSV file."""
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            # Match your CSV columns
            fieldnames = ['course_code', 'course_name', 'capacity', 'enrolled_students', 'waitlist']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for course in self.courses.values():
                enrolled_str = '|'.join(course.enrolled)
                waitlist_str = '|'.join(course.waitlist)
                writer.writerow({
                    'course_code': course.id,
                    'course_name': course.name,
                    'capacity': course.capacity,
                    'enrolled_students': enrolled_str,
                    'waitlist': waitlist_str
                })
        print(f"💾 Course data saved to {self.csv_file}.")

    def add_course(self, course_id, name, capacity):
        """Add a new course."""
        if course_id in self.courses:
            print(f"⚠️ Course {course_id} already exists.")
            return
        self.courses[course_id] = Course(course_id, name, capacity)
        print(f"✅ Added course: {name} ({course_id})")
        self.save_to_csv()

    def enroll(self, sid, course_id):
        """Enroll a student to a course or waitlist."""
        if course_id not in self.courses:
            print(f"⚠️ Course {course_id} not found.")
            return
        status = self.courses[course_id].enroll(sid)
        self.save_to_csv()
        return status

    def drop_student(self, sid, course_id):
        """Drop a student from a course."""
        if course_id not in self.courses:
            print(f"⚠️ Course {course_id} not found.")
            return
        self.courses[course_id].drop_student(sid)
        self.save_to_csv()

    def display_courses(self):
        """Display all courses with enrollment info."""
        print("\n--- Course Enrollments ---")
        for course in self.courses.values():
            print(f"{course.id} - {course.name}")
            print(f"  Capacity: {course.capacity}")
            print(f"  Enrolled: {list(course.enrolled)}")
            print(f"  Waitlist: {list(course.waitlist)}")



if __name__ == "__main__":
    scheduler = CourseScheduler(r"D:\projects\School management\sampledata\course.csv")

    # Display all courses from CSV
    scheduler.display_courses()

    # Enroll students
    scheduler.enroll("106", "CS101")
    scheduler.enroll("107", "CS101")
    scheduler.enroll("108", "CS101")  # Should go to waitlist if full

    # Drop a student to trigger waitlist processing
    scheduler.drop_student("101", "CS101")

    # Show final state
    scheduler.display_courses()


