import os
from Student_registry import StudentRegistry
from course_scheduling import CourseScheduler
from Fee_tracking import FeeBST, FeeRecord
from Library_system import LibrarySystem
from Perfomance_analytics import PerformanceAnalytics


# ----------- MAIN MENU SYSTEM -----------
def main():
    print("🎓 SCHOOL MANAGEMENT SYSTEM (Data Structures Project)")
    print("--------------------------------------------------")

    # File paths (adjust to your system)
    base_path = r"D:\projects\School management\sampledata"

    student_file = os.path.join(base_path, "students.csv")
    course_file = os.path.join(base_path, "courses.csv")
    fee_file = os.path.join(base_path, "fees.csv")
    library_file = os.path.join(base_path, "library.xlsx")
    performance_file = os.path.join(base_path, "performance.csv")

    # Initialize modules
    student_reg = StudentRegistry(student_file)
    course_sched = CourseScheduler(course_file)
    fee_tree = FeeBST(fee_file)
    library = LibrarySystem(library_file)
    perf_analyzer = PerformanceAnalytics(performance_file)

    # ---------- MENU LOOP ----------
    while True:
        print("""
==================== MAIN MENU ====================
1. 🎓 Student Registry
2. 📚 Library System
3. 💰 Fee Tracking
4. 📅 Course Scheduling
5. 📈 Performance Analytics
0. ❌ Exit
===================================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu(student_reg)
        elif choice == "2":
            library_menu(library)
        elif choice == "3":
            fee_menu(fee_tree)
        elif choice == "4":
            course_menu(course_sched)
        elif choice == "5":
            performance_menu(perf_analyzer)
        elif choice == "0":
            print("👋 Exiting system... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")


# ---------------- STUDENT MENU ----------------
def student_menu(student_reg):
    while True:
        print("""
----- STUDENT REGISTRY -----
1. View all students
2. Add new student
3. Search student by ID
4. Remove student
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            for student in student_reg.iterate_students():
                print(student)
        elif choice == "2":
            sid = input("Student ID: ")
            name = input("Name: ")
            year = input("Year: ")
            dept = input("Department: ")
            new_student = {"student_id": sid, "name": name, "year": year, "department": dept}
            try:
                student_reg.add_student(new_student)
                student_reg.save_to_csv()
            except ValueError as e:
                print(e)
        elif choice == "3":
            sid = input("Enter student ID: ")
            print(student_reg.get_student(sid) or "⚠️ Not found.")
        elif choice == "4":
            sid = input("Enter student ID to remove: ")
            if student_reg.remove_student(sid):
                student_reg.save_to_csv()
                print("✅ Student removed.")
            else:
                print("⚠️ Not found.")
        elif choice == "0":
            break


# ---------------- LIBRARY MENU ----------------
def library_menu(library):
    while True:
        print("""
----- LIBRARY SYSTEM -----
1. Display all books
2. Borrow book
3. Return last borrowed book
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            library.display_records()
        elif choice == "2":
            sid = input("Enter Student ID: ")
            bid = input("Enter Book ID: ")
            library.borrow_book(sid, bid)
        elif choice == "3":
            library.return_book()
        elif choice == "0":
            break


# ---------------- FEE MENU ----------------
def fee_menu(fee_tree):
    while True:
        print("""
----- FEE TRACKING -----
1. Display all records
2. Search fee record
3. Add new record
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            fee_tree.display_fees()
        elif choice == "2":
            sid = int(input("Enter Student ID: "))
            rec = fee_tree.search(sid)
            if rec:
                print(f"✅ Found: {rec.name}, Paid: {rec.amount_paid}, Balance: {rec.balance()}")
            else:
                print("⚠️ Student not found.")
        elif choice == "3":
            sid = input("Student ID: ")
            name = input("Name: ")
            paid = input("Amount Paid: ")
            total = input("Total Fee: ")
            new_record = FeeRecord(sid, name, paid, total)
            fee_tree.insert(new_record)
            fee_tree.save_to_csv()
            print("✅ Record added successfully.")
        elif choice == "0":
            break


# ---------------- COURSE MENU ----------------
def course_menu(course_sched):
    while True:
        print("""
----- COURSE SCHEDULING -----
1. Display all courses
2. Add new course
3. Enroll student
4. Drop student
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            course_sched.display_courses()
        elif choice == "2":
            cid = input("Course ID: ")
            name = input("Course Name: ")
            cap = int(input("Capacity: "))
            course_sched.add_course(cid, name, cap)
        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            course_sched.enroll(sid, cid)
        elif choice == "4":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            course_sched.drop_student(sid, cid)
        elif choice == "0":
            break


# ---------------- PERFORMANCE MENU ----------------
def performance_menu(perf_analyzer):
    while True:
        print("""
----- PERFORMANCE ANALYTICS -----
1. Display score matrix
2. Show average per subject
3. Show average per student
4. Show top performers
5. Show correlation heatmap
6. Show performance bar chart
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            perf_analyzer.get_score_matrix()
        elif choice == "2":
            perf_analyzer.average_per_subject()
        elif choice == "3":
            perf_analyzer.overall_average_per_student()
        elif choice == "4":
            perf_analyzer.top_performers(3)
        elif choice == "5":
            perf_analyzer.correlation_graph()
        elif choice == "6":
            perf_analyzer.bar_chart_top_students()
        elif choice == "0":
            break


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()

