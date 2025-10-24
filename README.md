# School-Management-System-Using-Data-Structure
class project to combine defferent modules so as to make a school management system


# 🏫 School Management System using Data Structures

A Python-based modular project that demonstrates the use of **fundamental data structures** — including stacks, queues, linked lists, binary search trees (BSTs), and heaps — to manage school operations such as student registration, fee tracking, course scheduling, library management, and performance analytics.

---

## 📘 Project Overview

This project was developed as part of the **Data Structures (CIT3200)** course at **Meru University of Science and Technology** under the guidance of **Mr. Dismas Kitaria**.

**Group Members:**  
👩‍💻 Prince • Hezle • Debra • Brayo  

---

## ⚙️ System Modules

| Module | File | Data Structure | Functionality |
|--------|------|----------------|----------------|
| 🎓 Student Registry | `student_registry.py` | Dictionary + Linked List | Register, view, delete, and search students |
| 📅 Course Scheduling | `course_scheduling.py` | Queue / Circular Array | Allocate students to courses, manage waitlists |
| 💰 Fee Tracking | `fee_tracking.py` | Binary Search Tree (BST) | Maintain sorted fee records, enable searching/reporting |
| 📚 Library System | `library_system_excel.py` | Stack (LIFO) | Manage book borrowing and returns |
| 📊 Performance Analytics | `performance_analytics.py` | Matrix / Heap / Graph | Analyze student marks and identify top performers |

---

## 🧩 System Architecture

+---------------------+
| main.py | ← Central Controller
+----------+----------+
|
+-----------------------------------+
| |
+----------v-----------+ +-------------------v----------------+
| Student Registry | | Course Scheduling (Queue) |
| Dict + Linked List | | Enroll & Waitlist Mgmt |
+----------+-----------+ +-------------------+----------------+
| |
+----------v-----------+ +-------------------v----------------+
| Fee Tracking (BST) | | Library System (Stack) |
| Sorted Fee Records | | Borrow & Return Books |
+----------+-----------+ +-------------------+----------------+
|
+----------v-----------+
| Performance Analytics|
| Graphs, Heaps, Matrix|
+----------------------+

yaml
Copy code

---

## 🧠 Data Structure Justification

| Function | Data Structure | Reason |
|-----------|----------------|--------|
| Student Lookup | Dictionary | O(1) average lookup |
| Course Enrollment | Queue | FIFO ensures fairness |
| Fee Records | BST | Sorted order for reporting |
| Library Borrowing | Stack | Tracks last borrowed/returned |
| Performance Analysis | Matrix + Heap | Efficient computation and ranking |

---

## 🗂️ Project Structure

School_Management_System/
│
├── main.py
├── student_registry.py
├── course_scheduling.py
├── fee_tracking.py
├── library_system_excel.py
├── performance_analytics.py
│
├── sampledata/
│ ├── students.csv
│ ├── courses.csv
│ ├── fees.csv
│ ├── library.xlsx
│ └── performance.csv
│
├── README.md
├── requirements.txt
└── School_Management_System_Final_Report.docx

---

## 📄 About the Project in Detail

[![Read Detailed Report](https://img.shields.io/badge/📘%20View%20Full%20Project%20Report-blue?style=for-the-badge)](https://docs.google.com/document/d/1VMICw_YiKzfSkjknxQgVLR2CKwdVgBXsvG5a7UsvxqE/edit?usp=sharing)

